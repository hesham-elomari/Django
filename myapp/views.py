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
from .models import Document
def base(request):
    return render(request,'myapp/base.html')

def fts(request):
    latest_question_list = Document.objects.order_by('description')[:200]
    return render(request,'myapp/files_to_see.html',{'latest_question_list':latest_question_list})

def upload(request):
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('myapp:files'))
        else:
            form = DocumentForm()
        return render(request, 'myapp/upload.html',{'form':form})


def download(file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    return response

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password1')
             user = authenticate(username=username, password=password)
             login1(request)
        return redirect(reverse('myapp:upload'))

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
            return HttpResponseRedirect(reverse('myapp:upload'))

    else:
        return render(request, 'myapp/login.html', {'form':AuthenticationForm})


def validate_file_extension(filename):
    x = 'Valid'
    if filename.name.endswith('.xlsx'):
        return x
    else: return 'not valid'

def logout1(request):
    if request.method == "GET":
        logout(request)
        return redirect(reverse('myapp:base'))
    else:
        return render(request,'myapp/login.html',{'form':AuthenticationForm})