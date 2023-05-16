from django.contrib import admin

from place.models import Answer, Comment, Option, Place

# Register your models here.


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "name",
        "latitude",
        "longitude",
        "description",
        "max_capacity",
        "address",
        "address_comment",
        "zipcode",
        "city_name",
        "country_name",
    )
    list_filter = ["name", "city_name"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "text",
        "author",
        "reply_to",
    )
    list_filter = ["author"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "start_date",
        "duration",
        "option",
        "created_by",
        "is_archived",
    )
    list_filter = []


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "name",
        "description",
        "created_by",
    )
    list_filter = []
