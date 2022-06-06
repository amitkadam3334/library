from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import CustomModelName, add,admininfo


def base (request):
    return render(request, 'lab.html')


def index(request ):
    a = CustomModelName()
    a.username = 'amit'
    b = a.username
    return render(request, 'index.html', {'username':b})


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        try:
            if User.username == username:
                pass
            else:
                myuser = User(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                myuser.save()
                messages.success(request, "your account has been succesfully created !")
        except:
            messages.error(request, "Username already taken !")
            return redirect("signup")



    return render(request, 'signup.html')


@csrf_exempt
def signin(request):

    if request.method == "POST":
        username = request.POST.get('username', False)
        pass1 = request.POST.get('pass1', False)
        print(User)
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)

            return render(request, 'index.html')
        else:
            messages.error(request, "bad credentials !")
            return redirect('signin')

    return render(request, 'signin.html')


def signup1(request):
    return render(request, 'signup.html')


def signout(request):
    logout(request)
    messages.success(request, 'logged out !!!')
    return redirect('signin')


def addbook(request):
    a = add.objects.all()
    print(a)
    if request.method == "POST":


        bookname = request.POST.get('bookname')
        authorname = request.POST.get('aname')
        publish_date = request.POST.get('pdate')
        ab = add(bookname=bookname, authorname=authorname, publishdate=publish_date)
        ab.save()
        messages.success(request, "Book has been added !")

        return render(request, 'index.html')
    else:
        return HttpResponse("<h1> 404 error !</h1>")

    return render(request, 'addbook.html')


def deletebook(request,**kwargs):

        id = kwargs['id']
        data = add.objects.filter(id=id)
        data.delete()
        messages.success(request, "Book Deleted !")


        return render(request, 'showbooks.html')


def updatebook(request,**kwargs):

    if request.method == "PUT":
        #id = request.PUT.get('id')
        bookname = request.PUT.get('bookname')
        authorname = request.PUT.get('aname')
        publish_date = request.PUT.get('pdate')
       # data = add.objects.filter(id=id)
        try:
            if add.bookname == bookname or add.authorname == authorname or add.publishdate == publish_date:
                ab = add(bookname=bookname, authorname=authorname, publishdate=publish_date)
                ab.save()
                messages.success(request, "Book Updated !")
                return render(request, 'updatebook.html')
        except:
            messages.error(request, "Book already upto date !")
            return render(request, 'updatebook.html')
    else:
        return HttpResponse("<h1> 404 error !</h1>")
        # messages.error(request, "request method is not put !")
        # return render(request, 'updatebook.html')


def update(request):
    return render(request, 'updatebook.html')

def showbook(request):
    if request.method == "GET":
        alldata = add.objects.all()
        data = {'data': alldata}
        return render(request,'showbooks.html',data)
    else:
        return HttpResponse("<h1> 404 error !</h1>")









