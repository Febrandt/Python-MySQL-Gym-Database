import mysql.connector
from DTO import Member, Payment

"""
Database Abstraction Classes for MySQL Database.
DAO stands for Data Access Object.
Bellow classes, will: retrieve, insert, delete, create any database data.
"""


class DAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
    


class Members(DAO):
    def __init__(self, connection):
        super().__init__(connection)

    def add_member(self, member: Member):
        sql = "INSERT INTO members (name, email, cpf, telephone) VALUES (%s, %s, %s, %s);"
        values = (member.name,member.email,member.cpf,member.telephone)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def remove_member(self, member_id: int):
        sql = f"DELETE FROM payments WHERE member_id = {member_id};"
        self.cursor.execute(sql)
        self.connection.commit()
        sql = f"DELETE FROM members WHERE id = {member_id};"
        self.cursor.execute(sql)
        self.connection.commit()
    
    def member_id_by_cpf(self,cpf: str) -> int:
        sql = "SELECT id FROM members WHERE cpf = %s;"
        value = (cpf,)
        self.cursor.execute(sql,value)
        return self.cursor.fetchone()[0]        


class Payments(DAO):
    def __init__(self, connection):
        super().__init__(connection)

    def add_payment(self, payment: Payment):
        sql = "INSERT INTO payments (member_id, month, year, payment_status) VALUES (%s, %s, %s, %s);"
        values = (payment.member_id, payment.month, payment.year, payment.payment_status)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def remove_payment(self, member_id: int, month: int, year: int):
        sql = "UPDATE payments SET payment_status = FALSE WHERE member_id = %s AND month = %s AND year = %s;"
        values = (member_id,month,year)
        self.cursor.execute(sql, values)
        self.connection.commit()
    
    def payment_payed(self, member_id: int, month: int, year: int) ->  bool:
        sql = "SELECT payment_status FROM payments WHERE member_id = %s AND month = %s AND year = %s;"
        values = (member_id,month,year)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()[0]