from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Business)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(User)