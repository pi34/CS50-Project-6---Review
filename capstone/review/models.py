from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage

from django.db import models


# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField("User", related_name="following")
    bio = models.TextField(blank=True, max_length=10000)

class Review(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=5000)
    likes = models.ManyToManyField("User", related_name="liked_reviews")
    business = models.ForeignKey("Business", on_delete=models.CASCADE, related_name="reviews")
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id, 
            "user": self.user.username,
            "title": self.title,
            "body": self.body,
            "likes": [like.username for like in self.likes.all()],
            "business_name": self.business.name,
            "business_id": self.business.id
        }

class Business(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, related_name="affiliations")
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=10000)
    image = models.FileField(blank=True, null=True, upload_to='images/')
    address = models.CharField(max_length=1000)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True, related_name="businesses")

    def __str__(self):
        return self.name
        
    def serialize(self):
        return {
            "id": self.id, 
            "user": self.user.username,
            "name": self.name,
            "body": self.description
        }

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "name": self.name, 
            "posts": self.businesses.all(),
            "id": self.id
        }