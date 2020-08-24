from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Publisher, Author
from .forms import BookForm, PublisherForm, AuthorForm

# Create your views here.
# need to put request as first arguement

def welcome(request):
   return HttpResponse("Welcome")

def index(request):
    # create a query set that has all the books like a cursor
    # like select * from SQL
    all_books = Book.objects.all()
    # first arguement always request and from template books folder
    return render(request, "books/index.template.html", {
        'all_books': all_books
    })

def show_publisher(request):
    all_publishers = Publisher.objects.all()
    return render(request, "books/show_publishers.template.html", {
        'all_publishers': all_publishers
    })

def show_author(request):
    all_authors = Author.objects.all()
    return render(request, "books/show_authors.template.html",{
        'all_authors': all_authors
    })


def create_book(request):
    # if user sumit data if not then display the form
    if request.method == "POST":
        # validate the form with no error in input
        submitted_form = BookForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(reverse(index))
    else:
    # from the forms.py to create a new instance from the class
        create_book_form = BookForm()
        return render(request, "books/create_book.template.html", {
            'form': create_book_form
        })

def create_publisher(request):
    if request.method == "POST":
        # 1. create the form with user input
        submitted_form = PublisherForm(request.POST)
        if submitted_form.is_valid():
            # 2. if submitted information is valid save
            submitted_form.save()
            return redirect(reverse(show_publisher))
    else:
        publisher_form = PublisherForm()
        return render(request, "books/create_publisher.template.html", {
            'form': publisher_form
    })

def create_author(request):
    if request.method == "POST":
        submitted_form = AuthorForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(reverse(show_author))

    else:
        author_form = AuthorForm()
        return render(request, "books/create_author.template.html", {
            'form': author_form
        })

def update_book(request, book_id):
    if request.method == "POST":
        # 1. retrieve the book that is being updated
        book_being_updated = get_object_or_404(Book, pk=book_id)
        # 2. do the modification !!!BIG POST!!!
        book_form = BookForm(request.POST, instance=book_being_updated)
        # 3. save if the form is valid
        if book_form.is_valid():
            book_form.save()
            # 4. redirect
            return redirect(reverse(index))
    else:
        # 1. retrive the book that we are editing
        book_being_updated = get_object_or_404(Book, pk=book_id)

        # 2. create the form containing the existing book's book data
        form = BookForm(instance=book_being_updated)

        # 3. display the form in a template
        return render(request, 'books/update_book.template.html', {
            'form': form
        })

def update_publisher(request, publisher_id):
    if request.method == "POST":
        publisher_being_updated = get_object_or_404(Publisher, pk=publisher_id)
        publisher_form = PublisherForm(request.POST,
                             instance=publisher_being_updated)
        if publisher_form.is_valid():
            publisher_form.save()
            return redirect(reverse(show_publisher))
    else:
        publisher_being_updated = get_object_or_404(Publisher, pk=publisher_id)
        form = PublisherForm(instance=publisher_being_updated)
        return render(request, 'books/update_publisher.template.html', {
            'form': form
        })

def update_author(request, author_id):
    if request.method == "POST":
        author_being_updated = get_object_or_404(Author, pk=author_id)
        author_form = AuthorForm(request.POST, instance=author_being_updated)
        if author_form.is_valid():
            author_form.save()
            return redirect(reverse(show_author))
    else:
        author_being_updated = get_object_or_404(Author, pk=author_id)
        form = AuthorForm(instance=author_being_updated)
        return render(request, 'books/update_author.template.html', {
            'form': form
        })

def delete_book(request, book_id):
    if request.method == "POST":
        book_to_delete = get_object_or_404(Book, pk=book_id)
        book_to_delete.delete()
        return redirect(reverse(index))
    # 1.fetch the book that we want to delete
    book_to_delete = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/delete_book.template.html', {
        'book': book_to_delete
    })

