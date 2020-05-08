from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from basic import forms, models
import pytesseract
from pytesseract import image_to_string
from basic.functions import ConvertPage

# Create your views here.

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def success(request,message=None):
    return render(request, 'messages/success.html')

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user: models.User = form.save(commit=False)
            password = models.User.objects.make_random_password()
            user.set_password(password)
            user.save()
            mail.send_mail(
              'User Registeration',
              'Welcome to my site:\nUserName: '+user.username+'\nYour Password is: ' + password,
              settings.EMAIL_HOST_USER,
                [form.cleaned_data.get('email')],

            )

            return render(request,'messages/register_success.html')
        else:
            return render(request, 'register_form.html', {'form': form})
    elif request.method == 'GET':
        form = forms.UserRegisterForm()
        return render(request,'register_form.html', {'form': form})

@login_required()
def get_view(request):
    if request.method == 'GET':
        form = forms.FileForm()
        return render(request, 'form.html', {'form': form})
    if request.method == 'POST':
        form = forms.FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['pdf_file']
            convertPageObj = ConvertPage(file)
            text = convertPageObj.get_result()
            each_line = text.split('\n\n')
            result = [(each_line[i], each_line[i + 1]) for i in range(0, len(each_line) - 1, 2)]
            return render(request, 'get_result.html', {'result': result})
        return render(request, 'form.html', {'form': form})
