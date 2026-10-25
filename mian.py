# main.py
# main.py
from books import load_books, save_books, display_books, delete_book
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def main():
    # Load existing books at the start
    books = load_books()
    
    while True:
        print("\n=== Personal Book Manager ===")
        print("1. View Books")
        print("2. Add a Book")
        print("3. Admin Mode")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            display_books(books)
            
        elif choice == "2":
            new_book = input("Enter the name of the book: ").strip()
            if new_book:
                books.append(new_book)
                save_books(books)
                print(f"'{new_book}' added successfully!")
            else:
                print("Book name cannot be empty.")
                
        elif choice == "3":
            # Admin Mode: Get password from environment variable
            admin_password = os.getenv("BOOK_MANAGER_ADMIN_PASSWORD")
            
            password = input("Enter admin password: ").strip()
            
            if password == admin_password:
                print("\n--- Welcome to Admin Mode ---")
                print("1. Delete a Book")
                print("2. Back to Main Menu")
                
                admin_choice = input("Choose admin option: ").strip()
                if admin_choice == "1":
                    delete_book(books)
                elif admin_choice == "2":
                    continue
                else:
                    print("Invalid admin option.")
            else:
                print("Incorrect password! Access denied.")
                
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
