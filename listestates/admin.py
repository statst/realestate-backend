from django.contrib import admin
from .models import Listestates
# Register your models here.
class ListestatesAdmin(admin.ModelAdmin):
    displayestate =('id', 'title','is_published', 'price', 'date', 'agent',)
    estate_links = ('id', 'title',)
    estate_filter = ('agent',)
    estate_published = ('is_published',)
    search_estate = ('title', 'description', 'address', 'city','state', 'zipcode', 'price' )
    list_per_page = 20

admin.site.register(Listestates, ListestatesAdmin)
