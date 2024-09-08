import sqlite3

# Function to create a new table
def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                 Name TEXT, 
                 Cell TEXT, 
                 Email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(name, cell, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''INSERT INTO contacts (Name, Cell, Email)
                 VALUES (?, ?, ?)''', (name, cell, email))
    conn.commit()
    conn.close()

# Function to fetch all data from the table
def fetch_all_data():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM contacts''')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Create table
create_table()

# Insert 5 rows of data
insert_data('John Doe', '1234567890', 'john@example.com')
insert_data('Jane Smith', '9876543210', 'jane@example.com')
insert_data('Alice Johnson', '5551234567', 'alice@example.com')
insert_data('Bob Brown', '9998887777', 'bob@example.com')
insert_data('Eve Green', '3334445555', 'eve@example.com')

# Fetch and display all data
print("All Contacts:")
fetch_all_data()

