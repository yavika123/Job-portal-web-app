from django.contrib import admin
from .models import Job, Application

# Register your models here.

class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0


class JobAdmin(admin.ModelAdmin):
    inlines = [ApplicationInline]
    
admin.site.register(Job)
admin.site.register(Application)
