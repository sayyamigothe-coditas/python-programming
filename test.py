import sqlite3


#connection to database
connection=sqlite3.connect("users.db")

#connection established
cursor=connection.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT
)

""")

#cursor is SQL Executor
#Create the cursor to process queries
# cursor.execute(
# "INSERT INTO users(name,email) VALUES(?,?)",
# ("sayyami","sam@gmail.com")
# )

#Commit the changes using the CONNECTION object
connection.commit()

#READ
cursor.execute("select * from users")


for user in cursor.fetchall():
    print(user)

#update
cursor.execute("update users set email=? where id=?",
("sayyami@gamlo.com",3)
)

connection.commit()




#delete
cursor.execute("delete from users where id=3")
connection.commit()

cursor.execute("select * from users")

for user in cursor.fetchall():
    print(user)


connection.close()