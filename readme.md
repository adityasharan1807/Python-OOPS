# Library Mangment System Using OOPS concept for Beginners

A simple library management system where you can manage books and members. The system will have functionalities such as
  * adding books,
  * registering members,
  * issuing books to members,
  * returning books.

## 1. What are classes ?
Classes: A class is a blueprint for creating objects. It defines a datatype by bundling data (attributes) and methods (functions) that operate on the data.

### Classes in  Library Managment System
1. Book
2. Member
3. Library




## 2. Relationships

Library - Book: A library has many books (one-to-many relationship).

Library - Member: A library has many members (one-to-many relationship).

Member - Book: A member can borrow many books (many-to-many relationship). This relationship is managed within the Library class by issuing and returning books.




## 3. What are objects ?
Objects: An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

Instances of the Book class represent individual books.
Instances of the Member class represent individual library members.
The Library class manages collections of Book and Member objects.

## 4. Attributes 
Attributes are variables that belong to a class. They represent the state or properties of a class and its objects.

Book Attributes: title, author, isbn, is_issued
Member Attributes: name, member_id, borrowed_books
Library Attributes: books, members

Instance atrributes inside init , the ones written like self.name =name and all.

## 5. Methods
Methods are functions defined within a class that describe the behaviors of the objects created from the class.

#### Book Method:
__str__(): Returns a string representation of a book.

#### Member Method:
__str__(): Returns a string representation of a member.

#### Library Methods:
add_book(book): Adds a book to the library.
register_member(member): Registers a new member.
issue_book(isbn, member_id): Issues a book to a member.
return_book(isbn, member_id): Returns a book from a member.


## OOPS principles in Library Mangagment:

### 1.Encapsulation
Encapsulation is the concept of bundling the data (attributes) and methods that operate on the data into a single unit, or class. It restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of the data.

In this project:

The Book, Member, and Library classes encapsulate their respective attributes and methods. This ensures that the data is manipulated only through the methods provided by the class.

### 2.Abstraction 

Abstraction means hiding the complex implementation details and showing only the necessary features of an object. It helps to reduce programming complexity and effort.

In this project:

The Library class provides methods to add books, register members, issue books, and return books. The internal implementation of how books and members are managed is hidden from the user.


### 3.Inheritance : 
Inheritance allows a class to inherit attributes and methods from another class. This helps to reuse the code and establish a relationship between classes.

Although inheritance is not explicitly used in this project, it could be applied, for example, to create specialized types of books (e.g., EBook, AudioBook) that inherit from a base Book class.

### 4.Polymorphism
Polymorphism allows methods to do different things based on the object it is acting upon, even though they share the same name. This can be achieved through method overriding or method overloading.

In this project, polymorphism could be implemented if we had different types of books or members that behave differently but share common method names. For example, a DigitalMember class could override the __str__() method to include additional digital library membership details.

## Summary
Classes and Objects: Structure your code with blueprints (classes) and create instances (objects).
* Attributes: Define the state of the objects.
* Methods: Define the behavior of the objects.
* Encapsulation: Bundle data and methods, restrict direct access to some components.
* Abstraction: Hide complex details and expose only the necessary parts.
* Inheritance: Create new classes based on existing ones to reuse code.
* Polymorphism: Methods do different things based on the object they act upon.
* Relationships: Model the "has-a" and "uses-a" relationships between classes.

## Future additions sugestions:
* Search functionality*: Add methods to search for books by title, author, or ISBN.
* Member history*: Keep a history of all books issued to and returned by each member.
* Fine calculation*: Implement fine calculation for late returns.
* GUI: Create a graphical user interface using libraries like Tkinter or PyQt.
