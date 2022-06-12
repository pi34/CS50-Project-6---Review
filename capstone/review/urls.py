from django.urls import path
from . import views

from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path("", views.index, name="index"), 
    path("login", views.login_view, name="login"), 
    path("register", views.register_view, name="register"), 
    path("logout", views.logout_view, name="logout"), 
    path("new", views.new, name="new"), 
    path("all/<str:data>", views.all, name="all"),
    path("business/<int:id>", views.business, name="business"),
    path("review/<int:id>", views.new_review, name="review"),
    path("category", views.category, name="category"),
    path("profile/<str:user>", views.profile, name="profile"),
    path("reviews/<str:data>", views.reviews, name="reviews")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)