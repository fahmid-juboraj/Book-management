from django.shortcuts import render, redirect,get_object_or_404, redirect
from .forms import BookForm
from .models import Book

def home(request):
    return render(request, 'home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=True)
            book.save()
            print("Inside the if")
            return redirect('book_list')
            
    else:
        print("Invalid")
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# from django.shortcuts import render, 
# from .forms import BookForm
# from .models import Book

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

# from django.shortcuts import render
# from .models import Book

def book_search(request):
    query_name = request.GET.get('name')
    query_age = request.GET.get('age')
    query_sci_fi = request.GET.get('sci_fi')
    query_drama = request.GET.get('drama')
    query_novel=request.GET.get('novel')

    if query_sci_fi and query_drama:
        query_set = Book.objects.filter(sci_fi=True, drama=True)
    elif query_sci_fi:
        query_set = Book.objects.filter(sci_fi=True)
    elif query_drama:
        query_set = Book.objects.filter(drama=True)
    else:
        query_set = Book.objects.all()

    if query_name:
        query_set = query_set.filter(name__icontains=query_name)

    if query_age:
        query_set = query_set.filter(publisher_age=query_age)

    return render(request, 'book_search.html', {'books': query_set})



