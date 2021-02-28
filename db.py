import psycopg2
import os
import logging

# os.environ['DATABASE_URL'] = "postgres://kblykrapdgouvd:9cf285ab17a34957d57a7486cdd8fc8981ac0825b56a4be9ec13e17ea1899ebb@ec2-54-220-35-19.eu-west-1.compute.amazonaws.com:5432/dcvocedv65tt72"
logging.basicConfig(level=logging.INFO)

def create_connection(path):
    conn = psycopg2.connect(path, sslmode='require')
    logging.info("Connection to Postgres DB successful")
    return conn


def execute_query(query):
    connection = create_connection(os.environ['DATABASE_URL'])
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def execute_read_query(query):
    connection = create_connection(os.environ['DATABASE_URL'])
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def save_remind(date, text, from_id):
    execute_query(f"INSERT INTO reminder (datetime, text, from_id) VALUES ('{date}', '{text}', {from_id})")


def delete_remind(date, text, from_id):
    execute_query(f"DELETE FROM reminder WHERE datetime='{date}' AND text='{text}' AND from_id={from_id}")


def save_message(m):
    execute_query(f"INSERT INTO history (chat_id, name, message, person_id) VALUES ({m.chat.id}, '{m.from_user.first_name}', '{m.text}', {m.from_user.id})")


def get_history(chat_id):
    return execute_read_query(f"SELECT name, person_id, message from history WHERE chat_id={chat_id}")


def init():
    execute_query(
     """
     CREATE TABLE IF NOT EXISTS reminder(
     id serial primary key,
     datetime varchar not null,
     text varchar not null, 
     from_id INTEGER not null);
     """)
    execute_query(
    """
    CREATE TABLE IF NOT EXISTS history(
    id serial primary key,
    chat_id varchar not null,
    name varchar not null,
    message varchar not null,
    person_id INTEGER not null);
    """)


def delete_history(chat_id):
    execute_query(
        """
        CREATE TABLE IF NOT EXISTS history_backup(
        id varchar primary key,
        chat_id INTEGER not null,
        name varchar not null,
        message varchar not null,
        person_id INTEGER not null);
        """)
    execute_read_query("""
    SELECT * FROM """)


conn = create_connection(os.environ['DATABASE_URL'])
