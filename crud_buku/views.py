from django.shortcuts import render, get_object_or_404, redirect
from .models import Buku

def index(request):
    books = Buku.objects.values().all()
    return render(request, 'index.html', {'books': books})

def show(request, id):
    book = get_object_or_404(Buku, pk=id)
    return render(request, 'show.html', {'book': book})

def add(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        language = request.POST.get('language')
        number_of_pages = request.POST.get('number_of_pages')
        stock = request.POST.get('stock')
        price = request.POST.get('price')
        
        # Create a new book instance
        buku = Buku(
            title=title,
            author=author,
            isbn=isbn,
            description=description,
            published_date=published_date,
            language=language,
            number_of_pages=number_of_pages,
            stock=stock,
            price=price
        )
        
        # Save the new book to the database
        buku.save()
        
        # Redirect to a success page or back to the index
        return redirect('index')
    
    return render(request, 'add.html')

def update(request, id):
    book = get_object_or_404(Buku, pk=id)
    
    if request.method == 'POST':
        # Retrieve form data from POST request
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        language = request.POST.get('language')
        number_of_pages = request.POST.get('number_of_pages')
        stock = request.POST.get('stock')
        price = request.POST.get('price')
        
        # Update the book instance
        book.title = title
        book.author = author
        book.isbn = isbn
        book.description = description
        book.published_date = published_date
        book.language = language
        book.number_of_pages = number_of_pages
        book.stock = stock
        book.price = price
        
        # Save the updated book to the database
        book.save()
        
        # Redirect to a success page or back to the index
        return redirect('index')
    
    return render(request, 'edit.html', {'book': book})

def delete(request, id):
    book = get_object_or_404(Buku, pk=id)
    if request.method == 'POST':
        book.delete()
        return redirect('index')