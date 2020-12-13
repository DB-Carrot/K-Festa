from django.contrib import admin
from festival.models import *

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ['festival_key', 'category_key', 'region_key', 'name', 'start_date', 'end_date']
    search_filds = ['festival_key']

@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ['format_key', 'format']
    search_filds = ['format']

@admin.register(FestivalCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_key', 'category_name']
    search_filds = ['category_name']

@admin.register(FestivalRegion)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_key', 'region_name']
    search_filds = ['region_name']


@admin.register(FestivalReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_key', 'festival_key', 'date']
    search_filds = ['review_key']



