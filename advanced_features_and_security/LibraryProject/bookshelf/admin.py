from django.contrib import admin
from .models import Book,CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
  list_display = ["email", "is_staff", "is_active"]
  list_filter = ["email", "is_staff", "is_active"]  
  fieldsets = ["is_active", "email", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publication_year"]
    list_filter = ["title", "author", "publication_year"]
    search_fields = ["title", "author", "publication_year"]
    ordering = ["publication_year"]
    fieldsets = (
        (None, {
            "fields": ("title", "author", "publication_year")
        }),
    )