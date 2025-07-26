from django.contrib import admin
from .models import Book,CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
  model = CustomUser
  list_display = ("email", "is_admin")
  list_filter = ("email", "is_admin") 
  search_fields = ["email"]
  filter_horizontal = ['groups', 'user_permissions']
  ordering = ["email"]
  readonly_fields = ["date_joined"]


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