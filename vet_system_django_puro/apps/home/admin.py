from django.contrib import admin
from .models import *

class ListandoUrls(admin.ModelAdmin):
    list_display = ('id', 'nome', 'urls')
    list_display_links = ('id', 'nome', 'urls')
    search_fields = ('id', 'nome', 'urls', 'grupo')
    list_per_page = 10
    
admin.site.register(Urls, ListandoUrls)