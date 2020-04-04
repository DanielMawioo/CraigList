from django.contrib import admin

# Register your models here.
from .models import Search


class SearchAdmin(admin.ModelAdmin):
    fields = ['search']

admin.site.register(Search, SearchAdmin)