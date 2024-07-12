from django.contrib import admin
from Frontpage.models import Visitor

# Register your models here.

@admin.register(Visitor)
class VisitorModelAdmin(admin.ModelAdmin):
    list_display = ['Key']