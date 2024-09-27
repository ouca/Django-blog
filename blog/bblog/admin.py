from django.contrib import admin
from .models import BigCategory, SmallCategory, Post

# Register your models here.
admin.site.register(BigCategory)
admin.site.register(SmallCategory)
admin.site.register(Post)
