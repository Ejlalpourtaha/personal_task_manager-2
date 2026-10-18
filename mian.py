# main.py
from books import display_books

def main():
    # Get user name
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! Welcome to the Book Manager.\n")
    
    # Get the number of books
    num_books_str = input("How many books would you like to enter? ")
    num_books = int(num_books_str)
    
    # Create an empty list to store book names
    books_list = []
    
    # Loop to get each book name
    for i in range(num_books):
        book_name = input(f"Enter the name of book #{i + 1}: ")
        books_list.append(book_name)
        
    # Call the function from books.py to display the books
    display_books(books_list)

if __name__ == "__main__":
    main()
