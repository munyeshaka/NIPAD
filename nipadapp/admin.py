from django.contrib import admin
from .models import *

admin.site.site_header  =  "NIPAD admin"  
admin.site.site_title  =  "NIPAD admin site"
admin.site.index_title  =  "NIPAD Admin"


class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'photo', 'body', 'date']
    
    # # explicitly reference fields to be shown, note image_tag is read-only
    # fields = ('title', 'image_tag', 'body',)
    # readonly_fields = ('image_tag',)


admin.site.register(Article,AdminArticle)

admin.site.register(Customer)