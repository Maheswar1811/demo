import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Maheswar@1211',
    database='testdb'
)
mycursor=mydb.cursor()
def add_user(name,age):
    sql="insert into students(name,age) values (%s,%s)"
    students=[(name,age)]
    mycursor.executemany(sql,students)
    mydb.commit()


def times():
    s="select * from students"
    mycursor.execute(s)
    res=mycursor.fetchall()
    return res
    


