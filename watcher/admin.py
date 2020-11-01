from django.contrib import admin
from watcher.models import Business, Neighborhood, Post, Profile

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)