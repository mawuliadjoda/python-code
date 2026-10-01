class Book:
    """ a class to model a book """
    
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.num_pages = 50  # Initialize number of pages to 0
        
    
    def read_book(self):
        print(f"You are reading {self.title} by {self.author}.")
    
    def describe_book(self):
        print(f"{self.title} is a {self.genre} book written by {self.author}.")
        
    def get_num_pages(self):
        print(f"{self.title} has {self.num_pages} pages.")
        
    def update_num_pages(self, new_num_pages):
        self.num_pages = new_num_pages
        print(f"Number of pages updated to {self.num_pages}.")
        
    def __str__(self):
        return (f"Book title: {self.title}, Author: {self.author}, Genre: {self.genre}")
 
 
class EBook(Book):
      def __init__(self, title, author, genre, file_size, format_):
        super().__init__(title, author, genre)
        self.file_format = "PDF"  # Default file format for e-books
        self.file_size = file_size
        self.format_ = format_
        
      def download_ebook(self):
        print(f"Downloading {self.title} in {self.file_format} format ({self.file_size} MB).")

#class MyEBook(Book):
#    def mytest(self):
#        print(self)
       
#book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
#
#
#book.update_num_pages(180)
#print(book)  # Output: book title
#print(book.get_num_pages())


#ebook = EBook(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction", file_size=2.5, format_="PDF")
#print(ebook)  # Output: book title
#
#print(ebook.download_ebook())  # Output: book title

#my_ebook = MyEBook(title="my ebook in 1984", author="George Orwell", genre="Dystopian")
#print(my_ebook)  # Output: book title