import pymysql

# Connect to MySQL server (without specifying database)
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',  # Change if you have a password
)

try:
    with connection.cursor() as cursor:
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS flask_auth_db")
        print("✓ Database 'flask_auth_db' created successfully!")
finally:
    connection.close()

print("\nNow you can run: python app.py")
