from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABSE = "webtags.db"


def create_connection(db_filename):
    try:
        connection = sqlite3.connect(db_filename)
        return connection

    except Error as e:
        print(e)
        return None





@app.route('/')
def home_page():

    query = "SELECT id, Player FROM web_tags"



    connection = create_connection(DATABSE)

    cursor = connection.cursor()
    cursor.execute(query)

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('index.html', data = data_list)

if __name__ == '__main__':
    app.run()
