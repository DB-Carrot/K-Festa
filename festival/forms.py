from django import forms
from .models import *

class FestivalForm(forms.ModelForm):
    
    class Meta:
        model = Festival
        fields = ('region_key','category_key','format_key', 'name', 'start_date', 'end_date', 'content') 


class ReviewForm(forms.ModelForm):

    class Meta:
        model = FestivalReview
        fields = ('content',)
