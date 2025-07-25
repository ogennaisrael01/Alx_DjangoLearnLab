from .models import Author, Book, Librarian, Library

    
def get_book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book)

def list_books_in_library(library_name):
    books = Library.objects.get(name=library_name)
    books.all()

def retrieve_liberian(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian
