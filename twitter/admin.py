from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)  # Unregister the default User model
admin.site.register(User, UserAdmin)  # Register the model with custom UserAdmin
admin.site.unregister(Group)
