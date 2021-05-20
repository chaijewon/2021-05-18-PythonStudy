# pip install cx_Oracle
import cx_Oracle
conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
cursor=conn.cursor() # 커서 오픈 
sql="""
     UPDATE python_student SET 
     name=:1 , kor=:2 , eng=:3 , math=:4
     WHERE hakbun=:5
    """
data=('홍길동 수정',80,90,75,1)
cursor.execute(sql,data)
conn.commit()
cursor.close()

cursor=conn.cursor()
sql="SELECT * FROM python_student"
cursor.execute(sql)
for row in cursor:
    print(row)
cursor.close()
conn.close()
