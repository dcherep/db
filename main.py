import psycopg
from psycopg.rows import dict_row

db_host='217.71.129.139'
db_port = 6075
db_user= 'admin'
db_pass = '12345'
db_name ='my_database'

conn=psycopg.connect(dbname=db_name, host=db_host, user=db_user, password=db_pass,port=db_port)
cursor=conn.cursor(row_factory=dict_row)

class Student:
    id=0
    name='Не указано'
    surname='Не указано'
    patr='Не указано'
    group_id=0
    group_name = 'Не указано'

    def get(self, student_id):
        sql='SELECT s.id, s.name, s.surname, s.patr, g.id AS group_id, g.title FROM students AS s JOIN groups AS g ON s.group_id = g.id WHERE s.id = %s'
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
        cursor.execute(sql, (self.id, self.name, self.surname,self.patr,self.group_id)) 
        conn.commit()      

    def edit(self,student_id):
        self.id = student_id
        self.name = input('Введите новое имя: ')
        self.surname =input('Введите новую фамилию: ')
        self.patr =input('Введите новое отчество: ')
        self.group_id =int(input('Введите новый id группы: ')  )
        sql = 'UPDATE students SET name=%s,surname=%s, patr=%s,group_id=%s WHERE id=%s'
        cursor.execute(sql, ( self.name, self.surname,  self.patr,self.group_id,self.id)) 
        conn.commit() 

    def delete(self,student_id):
        sql = 'DELETE FROM students AS s WHERE s.id = %s' 
        cursor.execute(sql, ( student_id,)) 
        conn.commit() 

    def print(self):
        print(f"| {self.id} | {self.surname} | {self.name} | {self.group_name} |")


def get_students():
    sql='SELECT * FROM students AS s JOIN groups AS g ON s.group_id=g.id ORDER BY s.surname ASC'
    cursor.execute(sql)
    for student in cursor.fetchall():
        print(f"| {student['surname']} | {student['name']} | {student['patr']} | {student['title']} |")

def get_student(student_id): 
    sql = f'SELECT * FROM students AS s JOIN groups AS g ON s.group_id = g.id WHERE s.id = {student_id}' 
    cursor.execute(sql) 
    student = cursor.fetchone() 
    print("-" * 30) 
    print(f"Фамилия: {student['surname']}")
    print(f"Имя: {student['name']}") 
    print(f"Отчество: {student['patr']}") 
    print(f"Группа: {student['title']}") 
    print ("-" * 30) 

def add_student(): 
    id = int(input('Введите id: ')) 
    surname = input('Введите фамилию: ') 
    name = input('Введите имя: ') 
    patr = input('Введите отчество: ') 
    group = input('Введите id группы: ') 
    sql = 'INSERT INTO students (id,surname,name,patr,group_id) VALUES (%s, %s, %s, %s, %s)' 
    cursor.execute(sql, (id, surname, name, patr,group)) 
   
    conn.commit()

def edit_student(student_id): 
    surname = input('Введите новую фамилию: ') 
    name = input('Введите новое имя: ') 
    patr = input('Введите новое отчество: ')
    group = input('Введите новый id группы: ') 
    sql = 'UPDATE students SET surname=%s, name=%s,patr=%s,group_id=%s WHERE id=%s' 
    cursor.execute(sql, (surname, name,patr,group, student_id)) 

    conn.commit() 


def delete_student(student_id): 
    sql = f'DELETE students WHERE s.id = {student_id}' 
    cursor.execute(sql, (student_id)) 

    conn.commit() 

print('1 - информация о студенте') 
print('2 - добавить студента') 
print('3 - редактировать студента') 
print('4 - отчислить студента') 
action = int(input('Введите действие: ')) 
if action == 1: 
    id=int(input('Введите id: '))
    student =Student()
    student.get(id)
    student.print() 
elif action == 2: 
    student = Student()
    student.create()
elif action == 3: 
    id = int(input('Введите id студента: ')) 
    student = Student()
    student.edit(id)
elif action == 4: 
    id = int(input('Введите id студента: ')) 
    student = Student()
    student.delete(id)
else: 
    print('Неверное действие')

cursor.close()
conn.close()


