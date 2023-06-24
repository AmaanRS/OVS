from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from . models import Candidate
import random
import string



# Create your views here.
def home(request):
    return render(request,'home/home.html')

def SignUp(request):
    if request.method =='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        param={'usrname':username,'password':password}
        if User.objects.filter(username=username) is None:
            myuser=User.objects.create_user(username=username,password=password)
            myuser.save()
            messages.success(request,'Your Account has been successfully created you can Login now ')
            return redirect("home")
        else:
            messages.success(request,'Username already exist')
            return redirect("home")
    else:
        return render(request,'home/error.html')

def Login(request):
    if request.method == 'POST':
        username=request.POST['Username1']
        password=request.POST['Password1']
        user=authenticate(username=username,password=password)
        allUsers=User.objects.all()
        name=User.objects.get(username=username)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in successfully ')
            request.session['name']='amaan'
            return redirect('VotePage')
        elif not name.is_active:
            messages.success(request,'You have already voted')
            return redirect("home")
        elif username not in allUsers :
            messages.success(request,'SignUp First')
            return redirect("home") 
        else:
            messages.success(request,'Use the right credentials')
            return redirect("home")    
    else:
        return render(request,'home/error.html')


def Logout(request):
        logout(request)
        messages.success(request,'Logged out of the account')
        return redirect("home")


def VotePage(request):
        if request.session.get('name') == 'amaan':
            allCandidates=Candidate.objects.all()
            params={'allCandidates':allCandidates}
            # del request.session['name']
            return render(request,'home/VotePage.html',params)
        else:
            return render(request,'home/error.html')


def VoteDone(request):
    if request.method == 'POST':
        id=request.POST['id']
        Candi=Candidate.objects.get(id=id)
        Candi.votes = Candi.votes + 1
        Candi.save()
        user = request.user
        user.is_active=False
        User.save(user)
        logout(request)
        messages.success(request,'You have voted and have been logged out of the account')
        return redirect('home')

    else:
        return render(request,'home/error.html')
        
def Search(request):
        if request.method == 'POST':
            Search=request.POST['Search']
            allCandidates=Candidate.objects.filter(username__icontains=Search)
            params={'allCandidates':allCandidates}
            return render(request,'home/VotePage.html',params)
        else:
            return render(request,'home/error.html')
