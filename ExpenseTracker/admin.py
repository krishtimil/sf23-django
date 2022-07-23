from django.contrib import admin
from ExpenseTracker import models
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'remarks')
    
    def name(self,obj):
        return obj;
admin.site.register(models.ExpenseRecord, AuthorAdmin)