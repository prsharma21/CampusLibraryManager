from abc import ABC, abstractmethod

class LibraryItem(ABC):
    total_items = 0 # class attribute, shared by every item

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True
        LibraryItem.total_items += 1

    def is_available(self):
        return self.__available
    
    def mark_borrowed(self):
        self.__available = False

    def mark_returned(self):
        self.__available = True

    @abstractmethod
    def late_fee(self):
        pass

class Book(LibraryItem):
    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
    
    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author}(ID {self.item_id})"

class Magazine(LibraryItem):
    DAILY_RATE = 1

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Magazine: {self.title} {self.issue_number} (ID {self.item_id})"

class DVD(LibraryItem):
    DAILY_RATE = 5

    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"DVD: {self.title} ({self.duration_minutes} mins) (ID {self.item_id})"

class Member:
    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []

    def borrow(self, item):
        if not isinstance(item, LibraryItem):
            raise ValueError("Invalid item type")
        if len(self.borrowed_items()) >= self.max_items:
            raise ValueError("Member has reached the maximum number of items")
        elif item == False or item.is_available() == False:
            raise ValueError(f"This item not available for borrowing by {self.name}")
        else:
            self.append_borrowed(item)
            item.mark_borrowed()
            print(f"Item borrowed by {self.name}:",item.describe())

    def return_item(self, item,days_late=0):
        if item.title not in self.borrowed_items() :
            raise ValueError(f"This item not borrowed by {self.name}")
        self.remove_borrowed(item)
        item.mark_returned()
        print(f"Item returned by {self.name}:",item.describe())
        return item.late_fee(days_late)
    
    def append_borrowed(self, item):
        self.__borrowed.append(item)

    def remove_borrowed(self, item):
        self.__borrowed.remove(item)

    def borrowed_items(self):
        return [item.title for item in self.__borrowed]
    
#print(LibraryItem.__available) #AttributeError: type object 'LibraryItem' has no attribute '__available'. Did you mean '.is_available' instead of '.__available'?
