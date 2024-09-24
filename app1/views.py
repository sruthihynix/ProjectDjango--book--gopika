from django.shortcuts import render,redirect
from app1.models import Book
# Create your views here.
def add_book(request):
    if request.method == 'POST':
        book = Book()   # Book Model name
        print(book)
        book.book_id = request.POST.get('book_id')
        book.book_name = request.POST.get('book_name')
        book.book_price = request.POST.get('book_price')
        book.book_image = request.POST.get('book_image')
        book.save()
        return redirect('/home')
    return render(request,'add.html')

def home(request):
    book = Book.objects.all()
    return render(request,'home.html', {'data':book})