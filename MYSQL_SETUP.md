# MySQL Database Setup Instructions

## Prerequisites
- XAMPP installed on your system
- Python 3.x installed

## Setup Steps

### 1. Start XAMPP Services
1. Open XAMPP Control Panel
2. Start **Apache** and **MySQL** services

### 2. Create Database
1. Open your browser and go to: `http://localhost/phpmyadmin`
2. Click on "New" in the left sidebar
3. Create a new database named: `flask_auth_db`
4. Click "Create"

### 3. Install Python Dependencies
Open a terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### 4. Configure Database Connection (Optional)
If you have a MySQL password set, update the connection string in `app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@localhost/flask_auth_db'
```

Default configuration (no password):
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_auth_db'
```

### 5. Run the Application
The database tables will be created automatically when you first run the app:

```bash
python app.py
```

The application will:
- Create the `users` and `admins` tables automatically
- Start on `http://127.0.0.1:5000`

## Database Tables Created

### Users Table
- `id` - Primary Key (Auto Increment)
- `username` - Unique username
- `password` - Hashed password
- `applied_courses` - Comma-separated list of courses

### Admins Table
- `id` - Primary Key (Auto Increment)
- `username` - Unique username
- `password` - Hashed password

## Troubleshooting

### Error: "Can't connect to MySQL server"
- Make sure MySQL is running in XAMPP
- Check that the database name is correct
- Verify your username/password in the connection string

### Error: "No module named 'pymysql'"
- Run: `pip install pymysql`

### Error: "Access denied for user 'root'@'localhost'"
- Check your MySQL root password
- Update the connection string with the correct password

## Migration Notes

### Changes from MongoDB to MySQL:
1. **Applied Courses Storage**: Changed from array to comma-separated string
2. **Auto-increment IDs**: MySQL uses integer primary keys instead of ObjectId
3. **Database Operations**: All MongoDB queries replaced with SQLAlchemy ORM
4. **Dependencies**: Replaced PyMongo with SQLAlchemy and PyMySQL

## Accessing the Application
- **User Registration**: `http://127.0.0.1:5000/register`
- **User Login**: `http://127.0.0.1:5000/login`
- **Admin Login**: `http://127.0.0.1:5000/admin/login`
- **Admin Registration**: `http://127.0.0.1:5000/admin/register`
