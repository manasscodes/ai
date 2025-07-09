# Using __init__ constructor
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print(f"{self.title} by {self.author}")

b1 = Book("AI for Beginners", "Andrew Ng")
b1.show()