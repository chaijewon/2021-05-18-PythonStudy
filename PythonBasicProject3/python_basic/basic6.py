import sqlite3
#연결 
conn=sqlite3.connect("student.db")
cur=conn.cursor()
'''
sql="""
      CREATE TABLE student(hakbun int,name text,
          kor int,eng int,math int)
    """
'''
#데이터 추가 
'''
sql="""
      INSERT INTO student VALUES(:hakbun,:name,:kor,:eng,:math)
    """
data={"hakbun":1,"name":'홍길동',"kor":90,"eng":80,"math":90} : Map 딕트 dict
cur.execute(sql,data)
print("데이터 추가 완료")
conn.commit()

sql="""
      INSERT INTO student VALUES(?,?,?,?,?)
    """
data=(2,'심청이',90,90,90) #튜플  [] => 리스트
cur.execute(sql,data)
cur.commit()
cur.close()
'''

data=[
       (3,'박문수',90,80,70),
       (4,'춘향이',80,90,60),
       (5,'이순신',90,90,90),
       (6,'강감찬',90,100,80),
       (7,'김두한',80,70,50)
     ]
sql="""
     INSERT INTO student VALUES(?,?,?,?,?)
    """
cur.executemany(sql,data)
conn.commit()
cur.close()
#데이터 읽기

cur=conn.cursor()
sql="SELECT * FROM student"
cur.execute(sql)
data=cur.fetchall()
for row in data:
    for i in row:
        print(i,end=" ")
    print('')
#print(data)
cur.close()
conn.close()










