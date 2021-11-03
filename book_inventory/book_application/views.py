from django.shortcuts import render,redirect
from book_application.models import Book
from book_application.forms import BookForm
# Create your views here.


def retrieve_books_view(request):
    books = Book.objects.all()
    return render(request,'book_application/index.html',{"books":books})

def create_book_view(request):
    form = BookForm()
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'book_application/insert_book.html',{"form": form})


def delete_book_view(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/')

def update_book_view(request,id):
    book = Book.objects.get(id=id)
    if request.method=="POST":
        form =  BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'book_application/update_book.html',{"book":book})
