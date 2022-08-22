from django.contrib import admin

from App_F.models import User, Post

class DjangoAdmin(admin.ModelAdmin):
    pass
admin.site.register(User)
admin.site.register(Post)


