from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all_list/', views.all_festival, name="festival"),
    path('category/', views.category, name="category"),
    path('category/category_list/<category_key>', views.category_list, name='category_list'),
    path('format/', views.format, name="format"),
    path('format/format_list/<format_key>', views.format_list, name='format_list'),
    path('location/', views.location, name="location"),
    path('location/location_list/<region_key>', views.location_list, name='location_list'),
    path('new_festival/', views.new_festival, name="new"),
    path('detail/<festival_key>/', views.detail_festival, name="detail"),
    path('edit/<festival_key>/', views.festival_edit, name="edit"),
    path('delete/<festival_key>/', views.festival_delete, name="delete"),
    path('detail/<festival_key>/review/', views.new_review, name="new_review"),
    path('detail/<festival_key>/review/delete/<review_key>/', views.delete_review, name="delete_review"),
]
