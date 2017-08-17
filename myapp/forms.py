from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from myapp.models import Document,User1
from myapp import models

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'user1')

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email',  'company_name' ,'job','password1', 'password2')

