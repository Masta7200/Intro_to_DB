import mysql.connector

try:
    # Connect to the MySQL server
    db = mysql.connector.connect(
        host="localhost",
        user="MySQLUser",  # Replace with your MySQL username
        password="12345"
    )

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    db.close()
