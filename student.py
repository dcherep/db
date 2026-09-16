import psycopg
from psycopg.rows import dict_row

class Student:
    conn=None

    def __init__(self, conn):
        self.conn=conn
        self.id=0
        self.name='Не указано'
        self.surname='Не указано'
        self.patr='Не указано'
        self.group_id=0
        self.group_name = 'Не указано'


    def get(self, student_id):
        sql='SELECT s.id, s.name, s.surname, s.patr, g.id AS group_id, g.title FROM students AS s JOIN groups AS g ON s.group_id = g.id WHERE s.id = %s'
        with self.conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql, (student_id,))
            student = cursor.fetchone()
            self.id = int(student['id'])
            self.name = student['name']
            self.surname =student['surname']
            self.patr =student['patr']
            self.group_id =student['group_id']
            self.group_name =student['title']

    def create(self):
        self.id = int(input('Введите id: '))
        self.name = input('Введите имя: ')
        self.surname =input('Введите фамилию: ')
        self.patr =input('Введите отчество: ')
        self.group_id =int(input('Введите id группы: ')  )
        sql = 'INSERT INTO students (id,name,surname,patr,group_id) VALUES (%s, %s, %s, %s, %s)' 
        with self.conn.transaction():
            with self.conn.cursor() as cursor:
                cursor.execute(sql, (self.id, self.name, self.surname,self.patr,self.group_id)) 
    

    def edit(self,student_id):
        self.id = student_id
        self.name = input('Введите новое имя: ')
        self.surname =input('Введите новую фамилию: ')
        self.patr =input('Введите новое отчество: ')
        self.group_id =int(input('Введите новый id группы: ')  )
        sql = 'UPDATE students SET name=%s,surname=%s, patr=%s,group_id=%s WHERE id=%s'
        with self.conn.transaction():
            with self.conn.cursor() as cursor:
                cursor.execute(sql, ( self.name, self.surname,  self.patr,self.group_id,self.id)) 


    def delete(self,student_id):
        sql = 'DELETE FROM students AS s WHERE s.id = %s' 
        with self.conn.transaction():
            with self.conn.cursor() as cursor:
                cursor.execute(sql, ( student_id,)) 

    def __str__(self):
        return f"| {self.id} | {self.surname} | {self.name} | {self.group_name} |"





