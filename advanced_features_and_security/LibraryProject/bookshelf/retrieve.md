RETRIEVE Book
from bookshelf.models import Book
Book.objects.get(title="1984")
Output:
('1984', 'George Orwell', 1949)

