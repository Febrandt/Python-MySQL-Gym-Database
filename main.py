import mysql.connector
import console_app
from DAO import DAO, Members, Payments
from DTO import Member, Payment

try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        database='gym'
    )
    print('Database Connection Made Succesfully!')
except mysql.connector.Error as error:
    print('Error Database Connection!')
    print(error)

members = Members(conn)
payments = Payments(conn)

console_app.run_console(members,payments)