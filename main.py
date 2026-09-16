import psycopg
from student import Student

db_host='217.71.129.139'
db_port = 6075
db_user= 'admin'
db_pass = '12345'
db_name ='my_database'

connection = psycopg.connect(dbname=db_name, host=db_host, user=db_user, password=db_pass,port=db_port)

print('1 - информация о студенте') 
print('2 - добавить студента') 
print('3 - редактировать студента') 
print('4 - отчислить студента') 
action = int(input('Введите действие: ')) 
if action == 1: 
    id=int(input('Введите id: '))
    student =Student(connection)
    student.get(id)
    print(student) 
elif action == 2: 
    student = Student(connection)
    student.create()
elif action == 3: 
    id = int(input('Введите id студента: ')) 
    student = Student(connection)
    student.edit(id)
elif action == 4: 
    id = int(input('Введите id студента: ')) 
    student = Student(connection)
    student.delete(id)
else: 
    print('Неверное действие')



