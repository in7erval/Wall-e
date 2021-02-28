import psycopg2
import os
import db

os.environ['DATABASE_URL'] = "postgres://kblykrapdgouvd:9cf285ab17a34957d57a7486cdd8fc8981ac0825b56a4be9ec13e17ea1899ebb@ec2-54-220-35-19.eu-west-1.compute.amazonaws.com:5432/dcvocedv65tt72"

with open('./history_files/history-1001335011853.txt') as f:
    for line in f.readlines():
        spl = line.split(' : ', 1)
        name = spl[0].split('[')[0]
        id = int(spl[0].split('[')[1][:-1])
        text = spl[1][:-1]
        chat_id = -432762228
        print(f'{name} {id} {text}')
        db.execute_query(f"INSERT INTO history (chat_id, name, message, person_id) VALUES ({chat_id}, '{name}', '{text}', {id});")