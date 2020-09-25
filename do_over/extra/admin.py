from django.contrib import admin
from .models import (
    City, Image, GoalOfSupport, Category, HotCategories, SendToEmail
)

admin.site.register(
    [
        City, Image, GoalOfSupport, Category, HotCategories, SendToEmail
    ]
)
