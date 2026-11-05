
Q1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
Ans: LibraryItem is abstract so it can share title, id. late_fee is an abstract method, which forces each child class to implement it and stops anyone from creating a bare LibraryItem. If DVD forgets late_fee(), DVD remains abstract, and creating a DVD raises a TypeError naming the missing method.

TypeError: Can't instantiate abstract class DVD without an implementation for abstract method 'late_fee'

Q2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Ans: 
Reading item.__available from outside the class raises AttributeError, because Python stores the name as _LibraryItem__available and outside code cannot see __available. is_available() is a method inside the class, so it can read that private flag and return it. We use the method so other code does not depend on the private name, and so availability changes only through mark_borrowed() and mark_returned().

AttributeError: type object 'LibraryItem' has no attribute '__available'. Did you mean '.is_available' instead of '.__available'?


Q3. What is the difference between LibraryItem.total_items and self.title?
Ans: LibraryItem.total_items is a class attribute: one counter shared by every book, magazine, and DVD, increased by 1 each time an item is created. self.title is an instance attribute: each object stores its own title, so two items can have different titles at the same time. Reading Book.total_items and DVD.total_items shows the same number, while book.title and dvd.title show two different strings