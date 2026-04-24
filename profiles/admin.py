from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_last_name',
        'default_email',
        'default_country',
    )


admin.site.register(UserProfile, UserProfileAdmin)
