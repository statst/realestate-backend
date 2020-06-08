from django.contrib import admin
from .models import Agent

# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 30

admin.site.register(Agent, AgentAdmin)