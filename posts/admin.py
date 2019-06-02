from django.contrib import admin

from . import models

admin.site.register(models.Post)


from posts.models import UserProfileInfo
from django.contrib.auth.models import User



admin.site.register(UserProfileInfo)