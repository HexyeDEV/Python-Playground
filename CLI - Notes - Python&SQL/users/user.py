import datetime
import hashlib
import users.sql_connection as connection

connect = connection.connect()
database = connect[0]
cursor = connect[1]

class User:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def register(self):
        date = datetime.datetime.now()

        cipher = hashlib.sha256()
        cipher.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES (null, %s, %s, %s, %s, %s)"
        user = (self.name, self.surname, self.email, cipher.hexdigest(), date)

        try:
            cursor.execute(sql, user)
            database.commit()
            return [cursor.rowcount, self]

        except:
            return [0, self]

    def identify(self):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        cipher = hashlib.sha256()
        cipher.update(self.password.encode('utf8'))

        user = (self.email, cipher.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result
