from django.contrib import admin
from .models import *
# Register your models here.
class Support(admin.ModelAdmin):
    readonly_fields=['image_preview']
admin.site.register(Support_Ticket,Support)