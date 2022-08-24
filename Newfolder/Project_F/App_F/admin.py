from django.contrib import admin

from App_F.models import User, Post

class userAdmin(admin.ModelAdmin):
    admin.site.register(User)

class postAdmin(admin.ModelAdmin):
    admin.site.register(Post)


