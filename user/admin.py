from django.contrib import admin
from user.models import Membership, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("uuid", "email", "first_name", "last_name", "is_active", "is_admin")
    list_filter = ["is_active", "is_admin"]


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        # "uuid",
        "user",
        "place",
        "role",
    )
