import sqlite3
from sqlite3 import Error


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn


def execute_query(query):
    connection = create_connection("db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(query):
    connection = create_connection("db.sqlite")
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def save_remind(date, text, from_id):
    execute_query(f"INSERT INTO reminder (datetime, text, from_id) VALUES ('{date}', '{text}', {from_id})")


def delete_remind(date, text, from_id):
    execute_query(f"DELETE FROM reminder WHERE datetime='{date}' AND text='{text}' AND from_id={from_id}")


def save_message(m):
    execute_query(f"INSERT INTO history (chat_id, name, message, person_id) VALUES ({m.chat.id}, '{m.from_user.first_name}', '{m.text}', {m.from_user.id})")


def get_history(chat_id):
    return execute_read_query(f"SELECT name, person_id, message from history WHERE chat_id={chat_id}")