import sqlite3

# Create database connection
connection = sqlite3.connect("contact.db")
print("Database opened successfully")

# Create table
connection.execute("CREATE TABLE IF NOT EXISTS contactdetails (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone_no TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")
print("Table created successfully")

# Close database connection
connection.close()
