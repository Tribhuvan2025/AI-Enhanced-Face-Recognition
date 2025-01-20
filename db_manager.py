import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    #drop table
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            regd_no VARCHAR(20),
            branch TEXT,
            student_type TEXT,
            course TEXT,
            college_name TEXT,
            student_image BLOB
        )
    """)
    conn.commit()
    conn.close()

# Register a new user
def register_user(name, email, regd_no, branch, student_type, course, college_name, student_image):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        # Read the image file as a binary stream
        if student_image is not None:
            student_image = student_image.read()

        cursor.execute("""
            INSERT INTO users (name, email, regd_no, branch, student_type, course, college_name, student_image) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, email, regd_no, branch, student_type, course, college_name, student_image))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def valid_user(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def fetch_user_data(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user
