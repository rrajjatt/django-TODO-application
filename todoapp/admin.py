from django.contrib import admin
from todoapp.models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Todo,TodoAdmin)