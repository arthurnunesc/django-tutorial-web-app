from django.contrib import admin

from .models import Todo, GoWishUser

admin.site.register(GoWishUser)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "importance",
        "deadline",
        "done",
    )
    search_fields = ("title",)
    list_filter = (
        "importance",
        "deadline",
    )
