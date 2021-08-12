import mysql.connector

def connect():

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="playground_mysql_python",
        port="3306"
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]
