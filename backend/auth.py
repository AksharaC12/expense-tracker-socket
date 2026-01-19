from db import get_db_connection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(name, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hash_password(password))
        )
        conn.commit()
        return True, "User registered successfully"
    except Exception as e:
        return False, "Email already exists"
    finally:
        cursor.close()
        conn.close()

def login(email, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT user_id, name FROM users WHERE email=%s AND password=%s",
        (email, hash_password(password))
    )
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return True, user
    else:
        return False, "Invalid credentials"
