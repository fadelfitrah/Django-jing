from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']

class TodoForm(forms.Form):
    title = forms.CharField(max_length=255, label="Judul Tugas")
    desc = forms.CharField(widget=forms.Textarea, label="Deskripsi", required=False)
    diselesaikan = forms.BooleanField(required=False, label="Selesai?")
