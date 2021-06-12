from django.contrib import admin
from .models import Document

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_display_links = ("title",)
    search_fields = ("title",)
    list_per_page = 25

admin.site.register(Document, DocumentAdmin)