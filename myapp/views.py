from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .forms import ModelFormWithFileField
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Task1.myapp.forms import SignUpForm

# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'files_to_see.html',{'form':form})
    else:
        form = DocumentForm()
        return render(request, 'upload.html', {'form': form})

def download(reuqest,dl_file):


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request,'files_to_see.html',{'form': form})
    else:
        form = UserCreationForm()
    return render(request,'registeration.html',{'form': form})


def validate_file_extension(filename):
    x = 'Valid'
    if filename.name.endswith('.xlsx'):
        return x
    else: raise ValidationError('Error message')
