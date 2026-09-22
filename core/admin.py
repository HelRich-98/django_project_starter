from django.contrib import admin

from .models import SiteInfo

# Register your models here.


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ("site_name", "site_logo", "site_favicon")
