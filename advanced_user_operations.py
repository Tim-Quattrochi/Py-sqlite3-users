import sqlite3
import uuid

new_uuid = uuid.uuid4()


def setup_database_schema():

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    with open('user.sql', 'r') as file:
        schema = file.read()
        cursor.executescript(schema)
        conn.commit()
    conn.close()


setup_database_schema()


def commit_and_close(conn):
    conn.commit()
    conn.close()


def create_user_with_profile(id, name, email, password, age, gender, address):

    try:
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (id, name, email, password, age, gender, address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (str(id), name, email, password, str(age), gender, address))
        commit_and_close(conn)

    except sqlite3.Error as e:
        print("An error occurred:", e)


def retrieve_users_by_criteria(min_age, max_age, gender):
    try:
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE age >= ? AND age <= ?  AND gender = ?", (str(min_age - 1), str(max_age), gender))
        users = cursor.fetchall()
        commit_and_close(conn)
        return users
    except sqlite3.Error as e:
        print("An error occurred:", e)
        return None


def update_user_profile(email, age, address):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET age = ?, address = ? WHERE email = ?", (str(age), address, email))
    commit_and_close(conn)


def delete_users_by_criteria(gender):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE gender = ?", (gender,))
    commit_and_close(conn)
