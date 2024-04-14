from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from.models import movie

# Create your views here.


def index(request):

    msg = " "
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            msg = "The username/password is incorrect"
    
        if user is not None:
            auth.login(request,user)
            return redirect('/home/')
    return render(request,'index.html',{'msg':msg}) 

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def home(request):
    mov = movie.objects.all()
    return render(request,'home.html',{'movies':mov})

@login_required(login_url='/')
def moviedetail(request,id):
    mov = movie.objects.get(id=id)
    return render(request,'moviedetail.html',{'moviedetail':mov})

@login_required(login_url='/')
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('search')
        # print(searched)
        sc  = movie.objects.filter(name__contains=searched)
        # print(sc)
        return render(request,'searched.html',{'searched':searched,'sc':sc})
    else:
        return render(request,'searched.html')