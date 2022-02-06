from django.contrib import admin
from .models import equipment


class equipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url')


admin.site.register(equipment,equipmentAdmin)
