from django import forms
from .models import STATUS_CHOICES, DEFAULT_STATUS


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя автора')
    email = forms.EmailField(max_length=100, required=True, label='Электронная почта')
    text = forms.CharField(max_length=2000, required=True, label='Отзыв', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, initial=DEFAULT_STATUS,
                               label='Статус')
