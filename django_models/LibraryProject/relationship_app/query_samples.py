from .models import Author, Book, Librarian, Library

    
def get_book_by_author(name):
    books = Book.objects.get(name=name)
    for book in books:
        print(book)

def list_books():
    books = Book.objects.all()

    for book in books:
        print(book)

def retrieve_liberian(name):
    liberian = Librarian.objects.select_related('library')
    print(liberian)
