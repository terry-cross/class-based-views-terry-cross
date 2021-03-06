from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Document
import datetime

# Create your views here.
    #DataFlair #Views #TemplateInheritance
# Create your views here.
def home(request):
    return render(request, 'base.html')
    
def other(request):
    context = {
    'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html', context)

def about(request):
    context = {
    'k2': 'Welcome to the Third page',
    }
    return render(request, 'about.html', context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

# def about(request):
#     time = datetime.datetime.now()
#     return render(request, 'about.html',{'time': time})