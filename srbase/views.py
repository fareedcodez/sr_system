from django.shortcuts import render

from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from pydoc_data.topics import topics
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import College, Repository,Title
from .form import RepositoryForm

# Create your views here.


def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username= request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')  
            
        user= authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')    
        else:
             messages.error(request, 'User or Password does not exist!')  
            
              
    context ={'page' : page}
    return render(request, 'srbase/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'srbase/login_register.html', {'form' : form})

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    repositories = user.repository_set.all()
    colleges = College.objects.all()
    
    context = {'user': user, 'repositories':repositories, 'colleges':colleges }
    return render(request, 'srbase/profile.html', context)

def collegePage(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    colleges = College.objects.filter(name__icontains=q)
    context={'colleges' : colleges}
    return render(request, 'srbase/community.html', context)

def titlePage(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    titles = Title.objects.filter(name__icontains=q)
    context={'titles' : titles}
    return render(request, 'srbase/titles_component.html', context)
    

def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    

    repositories = Repository.objects.filter(
        Q(college__name__icontains=q) |
        Q(title__name__icontains=q) |
        Q(description__icontains=q)
    )
    
    colleges= College.objects.all()
    repository_count= repositories.count()
    college_repositories = College.objects.all()
    
    
    context ={'repositories': repositories, 'colleges':colleges,  ' college_repositories':  college_repositories, 'repository_count': repository_count}
    return render(request, 'srbase/home.html', context)

def repository(request,pk):
    repository= Repository.objects.get(id=pk)
    context = {'repository': repository}
    return render(request, "srbase/repository.html", context)



def title(request):
     
    titles = Title.objects.all()
    context = {'titles' : titles}
    
    return render(request,'srbase/titles.html', context)

def authorsPage(request, pk):
     
    authors = User.objects.get(id=pk)
    context = {'authors' : authors}
    
    return render(request,'srbase/authors.html', context)
    
@login_required(login_url='login')
def createRepository(request):
    form = RepositoryForm()
    repositories= Repository.objects.all()
    if request.method == 'POST':
        form = RepositoryForm(request.POST, request.FILES)
        uploaded_file = request.FILES['docfile']
        print(uploaded_file.name)
        print(uploaded_file.size)
        
        if form.is_valid():
            repository = form.save(commit=False)
            repository.author = request.user
            repository.save()
            return redirect('home')
        
    context = {'form': form, 'repositories': repositories}
    return render(request, 'srbase/create_repository.html', context)

@login_required(login_url='login')
def updateRepository(request, pk):
    repository = Repository.objects.get(id =pk)
    form = RepositoryForm(instance=repository)
    
    if request.user != repository.author:
        return HttpResponse('Your are not Allowed here...!!')
        
    
    if request.method == 'POST':
        form = RepositoryForm(request.POST, instance=repository )
       
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request, 'srbase/create_repository.html', context)

@login_required(login_url='login')
def deleteRepository(request, pk):
    repository= Repository.objects.get(id =pk)
    
    if request.user != repository.author:
        return HttpResponse('Your are not Allowed here...!!')
    
    if request.method == 'POST':
        repository.delete()
        return redirect('home')
    return render(request, 'srbase/delete.html', {'obj':repository})
