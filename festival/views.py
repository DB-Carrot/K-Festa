import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ObjectDoesNotExist
from .forms import FestivalForm, ReviewForm


def index(request):
    return render(request, 'festival/index.html')

def category(request):
    categories = FestivalCategory.objects.all()
    return render(request, 'festival/category.html', {'categories':categories})

def category_list(request, category_key):
    category = get_object_or_404(FestivalCategory, category_key=category_key)
    festival_all = Festival.objects.filter(category_key=category_key).all()
    page_numbers_range = 9
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(festival_all,page_numbers_range)
    page = request.GET.get('page')
    festivals = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'festival/category_list.html',{'festival_all':festival_all, 'category':category, 'festivals':festivals, 'page_range':page_range, 'paginator':paginator })



def format(request):
    formats = Format.objects.all()
    return render(request, 'festival/format.html', {'formats':formats})

def format_list(request, format_key):
    format = get_object_or_404(Format, format_key=format_key)
    festival_all = Festival.objects.filter(format_key=format_key).all()
    page_numbers_range = 9
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(festival_all,page_numbers_range)
    page = request.GET.get('page')
    festivals = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'festival/format_list.html',{'festival_all':festival_all, 'format':format, 'festivals':festivals, 'page_range':page_range, 'paginator':paginator })


def location(request):
    locations = FestivalRegion.objects.all()
    return render(request, 'festival/location.html', {'locations':locations})

def location_list(request, region_key):
    location = get_object_or_404(FestivalRegion, region_key=region_key)
    festival_all = Festival.objects.filter(region_key=region_key).all()
    page_numbers_range = 9
    # 한 페이지에 나올 게시글 수
    paginator = Paginator(festival_all,page_numbers_range)
    page = request.GET.get('page')
    festivals = paginator.get_page(page)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'festival/location_list.html',{'festival_all':festival_all, 'location':location, 'festivals':festivals, 'page_range':page_range, 'paginator':paginator })


def festival_delete(request, festival_key):
    festival = get_object_or_404(Festival, festival_key=festival_key)
    festival.delete()
    return redirect(index)

def festival_edit(request, festival_key):
    festival = get_object_or_404(Festival, festival_key=festival_key)

    if request.method == 'POST': 
        form = FestivalForm(request.POST, instance=festival)
        if form.is_valid():
            festival = form.save()
            return redirect('/app/detail/'+str(festival.pk))
    else: 
        form = FestivalForm(instance=festival)

    return render(request, 'festival/edit_festival.html', {'form':form})


def new_festival(request):
    if request.method == 'POST': 
        form = FestivalForm(request.POST)
        if form.is_valid():
            festival = form.save()
            return redirect('/app/detail/'+str(festival.pk))
    else: 
        form = FestivalForm()
    return render(request, 'festival/new_festival.html', {'form':form})


def detail_festival(request, festival_key):
    festival = get_object_or_404(Festival, festival_key=festival_key)
    form = ReviewForm()
    review = FestivalReview()
    return render(request, 'festival/detail_festival.html',{'festival':festival,'form':form, 'review':review})

def new_review(request, festival_key):
    festival = get_object_or_404(Festival, festival_key=festival_key)
    form= ReviewForm(request.POST)
    if form.is_valid():
        review = FestivalReview()
        review = form.save(commit=False)
        review.festival_key = festival
        review.save()
    return redirect('/app/detail/'+str(festival.pk))

def delete_review(request, festival_key, review_key):
    festival = get_object_or_404(Festival, festival_key=festival_key)
    review = get_object_or_404(FestivalReview, review_key=review_key)
    review.delete()
    return redirect('/app/detail/'+str(festival.pk))
