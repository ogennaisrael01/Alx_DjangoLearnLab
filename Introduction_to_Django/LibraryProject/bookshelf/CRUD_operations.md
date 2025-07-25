# Bookshelf App - CRUD Operations

This app demonstrates basic CRUD (Create, Read, Update, Delete) operations using Django's ORM for a simple `Book` model.

## Usage

### Create
```python
book = Book(title="Half of a yellow sun", author="Chimanada Ngozi Adiche", publication_year="2006")
book.save()
```

### Read
```python
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
```

### Update
```python
book = Book.objects.get(title="Half of a yellow sun")
book.title = "1984"
book.author = "George Orwell"
book.publication_year = "1949"
book.save()
```

### Delete
```python
books = Book.objects.all()
books.delete()
```

## Output Example

After updating and deleting, your output will look like:

```
1984 George Orwell 1949
<QuerySet []>
```

See [CRUD_operations.md](CRUD_operations.md) for a step-by-step interactive example.
