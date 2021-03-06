from django.shortcuts import render
from .forms import NewBookForm,searchForm
from . import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def userLogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('http://localhost:8000/Books/view/')
        else:
            data['error']='Username or Password is invalid'
            return render(request,'books/user_login.html',data)
    else:
        return render(request,'books/user_login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('http://localhost:8000/Books/userlogin/')

@login_required(login_url='http://localhost:8000/Books/userlogin')
def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'books/view_books.html',{'books':books})
    return res

@login_required(login_url='http://localhost:8000/Books/userlogin')
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('http://localhost:8000/Books/view/')

@login_required(login_url='http://localhost:8000/Books/userlogin')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'books/edit_book.html',{'form':form,'book':book})
    return res

@login_required(login_url='http://localhost:8000/Books/userlogin')
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('http://localhost:8000/Books/view/')

@login_required(login_url='http://localhost:8000/Books/userlogin')
def searchBook(request):
    form=searchForm()
    res=render(request,'books/search_book.html',{'form':form})
    return res

@login_required(login_url='http://localhost:8000/Books/userlogin')
def search(request):
    form=searchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'books/search_book.html',{'form':form,'books':books})
    return res

@login_required(login_url='http://localhost:8000/Books/userlogin')
def insertBook(request):
    form=NewBookForm()
    res=render(request,'books/insert_book.html',{'form':form})
    return res

@login_required(login_url='http://localhost:8000/Books/userlogin')
def insert(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record Inserted Successfully <a href='http://localhost:8000/Books/view'>View Books</a>"
    return HttpResponse(s)
 


