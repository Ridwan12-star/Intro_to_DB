import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (no database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error while connecting to MySQL: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function
create_database()

