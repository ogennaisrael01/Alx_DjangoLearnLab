from .models import Author, Book, Librarian, Library

    
def get_book_by_author(name):
    books = Book.objects.get(name=name)
    for book in books:
        print(book)

def list_books(library_name):
    books = Library.objects.get(name=library_name)
    books.all()

def retrieve_liberian(name):
    liberian = Librarian.objects.get(name=name).select_related('library')
    print(liberian)
