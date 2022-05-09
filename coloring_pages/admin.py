from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

class Coloring_pageAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_html_photo', 'tema']
    list_editable = ['tema']
    search_fields = ['name', 'tema']
    list_filter = ['tema']
    prepopulated_fields = {'slug':('name',)}

    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

class TemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'cat']
    list_editable = ['content', 'cat']
    search_fields = ['name', 'content']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Coloring_page,Coloring_pageAdmin)
admin.site.register(Tema,TemaAdmin)
admin.site.register(Category,CategoryAdmin)
