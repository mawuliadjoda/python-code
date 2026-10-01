import book_generator

book = book_generator.Book(title="The Great Gatsby", 
                           author="F. Scott Fitzgerald", 
                           genre="Fiction drama")

ebook = book_generator.EBook(title="The Great Gatsby", 
                              author="F. Scott Fitzgerald", 
                              genre="Fiction drama", 
                              file_size=2.5, 
                              format_="PDF")

print(book.describe_book())  # Output: Book title: The Great Gatsby, Author: F. Scott Fitzgerald, Genre: Fiction
print(ebook.download_ebook())  # Output: Downloading The Great Gatsby in PDF format (2.5 MB).