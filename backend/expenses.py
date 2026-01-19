from db import get_db_connection

def add_expense(user_id, category_id, amount, note, expense_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (user_id, category_id, amount, note, expense_date)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (user_id, category_id, amount, note, expense_date)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return True

def get_expenses(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT e.expense_id, c.name AS category, e.amount, e.note, e.expense_date
        FROM expenses e
        JOIN categories c ON e.category_id = c.category_id
        WHERE e.user_id = %s
        ORDER BY e.expense_date DESC
        """,
        (user_id,)
    )

    expenses = cursor.fetchall()
    cursor.close()
    conn.close()

    return expenses

def delete_expense(expense_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE expense_id=%s AND user_id=%s",
        (expense_id, user_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return True
