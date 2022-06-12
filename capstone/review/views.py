from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.forms import ModelForm, Textarea
from django.db.models import Avg

from .models import *

import json
import time

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'image', 'address', 'category']
        widgets = {
            'description': Textarea(attrs={'cols':80, 'row':20}),
        }

# Create your views here.
def index (request):
    if request.user.is_authenticated:
        return render(request, "review/profile.html", {
            'user': request.user
        })

    else:
        return HttpResponseRedirect(reverse("login"))


@csrf_exempt
def profile (request, user):
    user = User.objects.get(username=user)
    if request.method == "PUT":
        if request.user in user.followers.all():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        return HttpResponse(status=204)
    else:
        return render(request, "review/profile.html", {
            'user': user
        })
    

def all (request, data):
    if data == 'review':
        return render(request, "review/all.html", { 'review': True })
    elif data == 'search':
        return render(request, "review/all.html", { 'category': data, 'location': request.GET.get("location")})
    else:
        return render(request, "review/all.html", { 'category': data })


def reviews (request, data):
    if data == 'review':
        reviews = Review.objects.all()
        reviews = reviews.order_by("-timestamp").all()

    else:
        if data == 'all':
            reviews = Business.objects.all()
        elif data == 'search':
            reviews = Business.objects.filter(address__contains=request.GET.get("location"))
        else:
            category = Category.objects.get(name=data)
            reviews = Business.objects.filter(category=category)

        reviews = reviews.annotate(ratings=Avg('reviews__rating')).order_by("-ratings")

    start = int(request.GET.get("start") or 0)

    time.sleep(1)

    p = Paginator(reviews, 5)
        
    page = p.page(start)
    set_reviews = page.object_list

    return JsonResponse([review.serialize() for review in set_reviews], safe=False)


@csrf_exempt
@login_required(login_url='/login')
def business (request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        body = data.get("body")
        review = Review.objects.get(id=id)
        if body is not None:
            review.body = body
        else:
            if request.user in review.likes.all():
                review.likes.remove(request.user)
            else:
                review.likes.add(request.user)
        review.save()
        return HttpResponse(status=204)
    else:
        return render(request, "review/business.html", {
            'business': Business.objects.get(pk=id)
        })


@csrf_exempt
def category (request):
    return JsonResponse({"categories": [category.name for category in Category.objects.all()]})



@csrf_exempt
@login_required(login_url='/login')
def new_review (request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get("title")
        rating = data.get("rating")
        body = data.get("body")

        review = Review(user=request.user, title=title, rating=rating, body=body, business=Business.objects.get(id=id))
        review.save()

        return HttpResponse(status=204)
        

@csrf_exempt
@login_required(login_url='/login')
def new (request):

    if request.method == 'POST': 
        form = BusinessForm(request.POST, request.FILES) 
        if form.is_valid(): 
            if request.user.is_authenticated:
                new = form.save(commit=False) 
                new.user = request.user
                new.save()
        return HttpResponseRedirect(reverse("business", kwargs={'id':new.id}))
    else: 
        form = BusinessForm() 
    return render(request, 'review/new.html', {'form' : form}) 


def login_view (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "review/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "review/login.html")


def register_view (request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "review/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "review/register.html")


def logout_view (request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))