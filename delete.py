import sqlite3

conn = sqlite3.connect("users.db")

print("Opened DB Connection")

user_id - input("enter and ID to Delete: \n")
conn.execute(f"DELETE FROM EMPLOYEES where ID = {user_id}")

conn.commit()
print("Data delete Seccess")
conn.close()