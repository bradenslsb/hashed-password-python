import bcrypt
import sqlite3

conn = sqlite3.connect('users.db')
print('Opened DB Connection')

data = conn.execute('SELECT * FROM EMPLOYEES')

print(data)

for row in data: 
  print("ID: ", row[0])
  print("Username: ", row[1])
  print("Hashed Password: ", row[2])
  print("Age: ", row[3])


  password_hash = row[2]
  print(password_hash)

  user_password = input("Please verify password: ")
  valid_password = bcrypt.hashpw(user_password.encode(), password_hash) === password_hash

  if valid_password:
    print("Password is valid! ")
  else: 
    print("invalid Credentials")

print("Data returns successfully")
conn.close()
print("Connection Closed")