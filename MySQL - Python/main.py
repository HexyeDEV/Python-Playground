import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="playground_mysql_python"
)

cursor = database.cursor(buffered=True)

# cursor.execute("CREATE DATABASE IF NOT EXISTS playground_mysql_python")
# cursor.execute("SHOW DATABASES")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehicles(
    id int(10) auto_increment not null,
    brand varchar(40) not null,
    model varchar(40) not null,
    price float(10,2) not null,
    constraint pk_vehicle PRIMARY KEY(id)
    )
""")

# cursor.execute("SHOW TABLES")
# for table in cursor:
#   print(table)

# cursor.execute("INSERT INTO vehicles values(null, 'Volkswagen', 'Taos', '18000')")
# database.commit()  # Save the changes done to the DB by the cursor

# cars = [
#     ('Seat', 'Ibiza', '16000'),
#     ('Chevrolet', 'Spark', '12000'),
#     ('BMW', '320i', '32000'),
#     ('Ford', 'Fusion', '20000'),
# ]

# cursor.executemany("INSERT INTO vehicles VALUES (null, %s, %s, %s)", cars)
# database.commit()

# cursor.execute("SELECT * FROM vehicles WHERE price <= 20000 AND brand = 'Seat'")
# vehicles = cursor.fetchall()
# for vehicle in vehicles:
#    print(vehicle[0], vehicle[1])

# cursor.execute("SELECT * FROM vehicles")
# vehicle = cursor.fetchone()
# print(vehicle)

# cursor.execute("DELETE FROM vehicles WHERE brand = 'Chevrolet' ")
# database.commit()
# print(cursor.rowcount, "deleted elements")

# cursor.execute("UPDATE vehicles SET model='Leon' WHERE brand='Seat'")
# database.commit()
# print(cursor.rowcount, "updated elements")

cursor.execute("SELECT * FROM vehicles")
vehicles = cursor.fetchall()
for vehicle in vehicles:
    print(vehicle)
