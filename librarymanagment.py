import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="library_db"
)

cursor = db.cursor()

def add_book(title, author, genre, year_published, quantity):
    sql = "INSERT INTO books (title, author, genre, year_published, quantity) VALUES (%s, %s, %s, %s, %s)"
    val = (title, author, genre, year_published, quantity)
    cursor.execute(sql, val)
    db.commit()
    print(f"Book '{title}' added successfully!")

def add_member(name, email):
    sql = "INSERT INTO members (name, email, join_date) VALUES (%s, %s, %s)"
    val = (name, email, date.today())
    cursor.execute(sql, val)
    db.commit()
    print(f"Member '{name}' added successfully!")

def borrow_book(book_id, member_id, quantity):
    cursor.execute("SELECT quantity FROM books WHERE id = %s", (book_id,))
    result = cursor.fetchone()
    if result and result[0] >= quantity:
        sql = "UPDATE books SET quantity = quantity - %s WHERE id = %s"
        cursor.execute(sql, (quantity, book_id))
        db.commit()
        sql = "INSERT INTO borrow (book_id, member_id, borrow_date, quantity) VALUES (%s, %s, %s, %s)"
        val = (book_id, member_id, date.today(), quantity)
        cursor.execute(sql, val)
        db.commit()
        print("Book loaned successfully!")
    else:
        print("Book is not available in the desired quantity. Available Quantity is :",quantity)


def return_book(loan_id, quantity):
    sql = "UPDATE borrow SET return_date = %s WHERE id = %s"
    val = (date.today(), loan_id)
    cursor.execute(sql, val)
    db.commit()
    sql = "UPDATE books SET quantity = quantity + %s WHERE id IN (SELECT book_id FROM borrow WHERE id = %s)"
    cursor.execute(sql, (quantity, loan_id))
    db.commit()
    print("Book returned successfully!")

def view_books():
    cursor.execute("SELECT * FROM books")
    for book in cursor.fetchall():
        print(book)

def view_members():
    cursor.execute("SELECT * FROM members")
    for member in cursor.fetchall():
        print(member)

def view_borrows():
    cursor.execute("SELECT * FROM borrow")
    for borrow in cursor.fetchall():
        print(borrow)

# Example usage
if __name__ == "__main__":
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Borrows")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            year_published = int(input("Enter year published: "))
            quantity = int(input("Enter quantity: "))
            add_book(title, author, genre, year_published, quantity)
        elif choice == 2:
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            add_member(name, email)
        elif choice == 3:
            book_id = int(input("Enter book ID: "))
            member_id = int(input("Enter member ID: "))
            quantity = int(input("Enter quantity to borrow: "))
            borrow_book(book_id, member_id, quantity)
        elif choice == 4:
            loan_id = int(input("Enter loan ID: "))
            quantity = int(input("Enter quantity to return: "))
            return_book(loan_id, quantity)
        elif choice == 5:
            view_books()
        elif choice == 6:
            view_members()
        elif choice == 7:
            view_borrows()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")


db.close()
