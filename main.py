from models import Book, Magazine, DVD, Member, LibraryItem

class Library:
    def __init__(self):
        book = Book("Python Programming", "IT12", "John Doe")
        magazine = Magazine("Python Monthly", "IT34", 111223)
        dvd = DVD("Python in 60 Minutes", "IT45", 60)

        alice = Member("Alice","MEM123")
        bob = Member("Bob","MEM456",1)
        
        for item in [book, magazine, dvd]:
                late_fee = item.late_fee(3)
                print(item.describe(),"-> late fee for 3 days: Rs",late_fee)
        try:
            #phase 1:
            print("Phase 1:")
            alice.borrow(book)  
            alice.borrow(magazine) 
            alice.borrow(dvd)

            alice.return_item(dvd)

            bob.borrow(dvd)
            
            bob.borrow(book) 
        except ValueError as e:
            print("Could not borrow:",e)
           
        try:
            #phase 2:
            print("Phase 2:")
            bob.return_item(book)
            
        except ValueError as e:
            print("Could not return:",e)
            
        try:
            print("Phase 3:")
            alice.borrow(book)
        except ValueError as e:
            print("Could not borrow:",e)

        try:
            print("Phase 4:")
            late_fee = alice.return_item(book,2)
            print("Late fee for Alice for returning book: Rs",late_fee)
        except ValueError as e:
            print("Could not borrow/return:",e)
            
        print("Total items created:", LibraryItem.total_items)

Library()     



