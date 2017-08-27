from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import  HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render,redirect,reverse
from myapp.forms import DocumentForm, SignUpForm
import os.path
from django.utils.encoding import smart_str
from task import settings
import mimetypes
from wsgiref.util import FileWrapper
from .models import Document, User1
from os.path import isfile, getsize
from rest_framework.generics import ListAPIView,CreateAPIView

def base(request):
    return render(request,'myapp/base.html')

def fts(request):
    latest_question_list = Document.objects.order_by('description')[:200]
    return render(request,'myapp/files_to_see.html',{'latest_question_list':latest_question_list})

def upload(request):
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            x = request.FILES['document'].name
            z = request.FILES['document']
            if z.name.endswith('.xlsx'):
                if isSQLite3(x) is  False:
                    if form.is_valid():
                       form.save()
                    return redirect(reverse('myapp:files'))
            else: form = DocumentForm()
            return render(request, 'myapp/upload.html',{'form':form})
        else:
            form = DocumentForm()
        return render(request, 'myapp/upload.html',{'form':form})

def download(request,filename):
    file_path = settings.MEDIA_ROOT +'/'+ filename
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    return response

def isSQLite3(filename):
    if not isfile(filename):
        return False
    if getsize(filename) < 100: # SQLite database file header is 100 bytes
        return False

    with open(filename, 'rb') as fd:
        header = fd.read(100)

    return header[:16] == 'SQLite format 3\x00'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password1')
             user = authenticate(username=username, password=password)
        return redirect(reverse('myapp:base'))

    else:
        form = SignUpForm()
    return render(request,'myapp/registeration.html',{'form': form})

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:

             login(request, user)
             if (user.job == 'Admin'):
                return HttpResponseRedirect(reverse('myapp:upload'))
             else: return HttpResponseRedirect(reverse('myapp:files'))
    else:
        return render(request, 'myapp/login.html', {'form':AuthenticationForm})

def validate_file_extension(file):
    if file.name.endswith('.xlsx'):
        x = 'Valid'
    else: x = 'Fail'

def logout1(request):
    if request.method == "GET":
        logout(request)
        return redirect(reverse('myapp:base'))
    else:
        return render(request,'myapp/login.html',{'form':AuthenticationForm})

