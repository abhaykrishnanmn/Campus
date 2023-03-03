from polls.models import Question
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from pages.models import Profile
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup 
import requests
import urllib.request








# Create your views here.


def home(request):
    return render(request, 'pages/home.html')

def landing(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pages/fests.html', context)

def user_login(request):
    print('hello')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('/login')
    else:
        return render(request,'userreg/login.html')

def user_logout(request):
    logout(request)
    messages.success(request,("You Were Logged Out!"))
    return redirect('/')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if password.isnumeric():
            messages.info(request,'Password should include atleast one alphabet')
            return redirect(user_signup)
        elif password.isalpha():
            messages.info(request,'password should include atleast one number')
            return redirect(user_signup)
        hashed_password = make_password(password)
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.info(request,'Already have an account with same email id')
            return redirect(user_signup)
        else:
            user = User(username=username,password=hashed_password,email=email)
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect('/home')
    return render(request,'userreg/signup.html')

@login_required(login_url='/auth/login')
def profile(request):
    all_data = User.objects.all()
    return render(request,'pages/profile.html', {'key':all_data})

@login_required(login_url='/auth/login')
def editprofile(request):
    if request.method == 'POST':
        ph_num1 = request.POST.get('ph_num')
        addr1 = request.POST.get('addr')
        clg_name1 = request.POST.get('clg_name')
        sem1 = request.POST.get('sem')
        brch1 = request.POST.get('brch')
        cgpa1 = request.POST.get('cgpa')
        bklgs1 =request.POST.get('bklgs')
        website1 = request.POST.get('website')
        github1 = request.POST.get('github')
        linkedin1 = request.POST.get('linkedin')
        stkoflw1 = request.POST.get('stkoflw')
        codechef1 = request.POST.get('codechef')
        dp_img1 = request.FILES.get('dp_img')
        
        Prof = Profile.objects.get(user=request.user)
        profile = Profile(ph_num=ph_num1 if ph_num1 else Prof.ph_num,addr=addr1 if addr1 else Prof.addr,clg_name=clg_name1 if clg_name1 else Prof.clg_name,sem=sem1 if sem1 else Prof.sem,brch=brch1 if brch1 else Prof.brch,cgpa=cgpa1 if cgpa1 else Prof.cgpa,bklgs=bklgs1 if bklgs1 else Prof.bklgs,website=website1 if website1 else Prof.website,github=github1 if github1 else Prof.github,linkedin=linkedin1 if linkedin1 else Prof.linkedin,stkoflw=stkoflw1 if stkoflw1 else Prof.stkoflw,codechef=codechef1 if codechef1 else Prof.codechef,dp_img=dp_img1 if dp_img1 else Prof.dp_img,user=request.user)
        profile.save()
        return redirect('/profile')
    return render(request,'pages/editprofile.html')

@login_required(login_url='/auth/login')
def offc(request):
    try:
        urllib.request.urlopen('http://google.com') 
        i=1
        s='{% extends "../pages/base.html" %}{% load static %}{% block title %}Off Campus{% endblock title %}{% block head %}<link rel="stylesheet" href="/static/offc.css">{% endblock head %}'
        b='{% block body %}'
        be='{% endblock body %}'
        c='<link href="/static/offc.css" rel="stylesheet" type="text/css" />'
        html_text=requests.get('https://www.offcampusjobsite.com/').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li',class_ ='')
        with open(f'templates\pages\offc.html','w') as f :
            f.write(f"{s}\n")
            f.write(f"<!DOCTYPE html>\n")
            f.write(f"<html>\n")
            f.write(f"<head>\n")
            f.write(f"<title>Off_Campus_Drive</title>\n")
            f.write(f"{b}\n")
            f.write(f"{c}\n")
            f.write(f"</head>\n")
            f.write(f"<body>\n")
            f.write(f"<h1><br><br>Off Campus Drives</h1>\n")
            for job in jobs:
                company_name = job.find('a',class_ ='wp-block-latest-posts__post-title').encode('utf-8')
                more_info = job.find('div',class_ ='wp-block-latest-posts__post-excerpt').text.encode('utf-8')
                c=company_name.decode('ascii','ignore')
                m=more_info.decode('ascii','ignore')
                f.write(f"<h2> Company : {i}</h2>\n")
                f.write(f"<p>{m.strip()}</p>\n")
                f.write(f"<h3> {c} </h3> \n ")
                f.write(f"<br>")
                i+=1
            f.write(f"</body>\n")
            f.write(f"</html>\n")
            f.write(f"{be}\n")
        f.close()
    except:
        with open(f'templates\pages\offc.html','w') as f :
            f.write(f"<h1>Check your internet connectivity</h1>\n")
    return render(request,'pages/offc.html')

def test(request):
    return render(request, 'pages/test.html')

def learn(request):
    return render(request, 'pages/learn.html')