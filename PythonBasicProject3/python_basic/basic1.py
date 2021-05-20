#오라클 (sqlite)
import cx_Oracle
# 1. 연결 
conn=cx_Oracle.connect("hr/happy@localhost:1521/XE")
# 2. 전송하고 데이터를 받는 객체 
cursor=conn.cursor()
item=[
  ('홍길자',90,80,70),
  ('을지문덕',80,80,67),
  ('이순신',90,90,90),
  ('김두한',80,80,70),
  ('춘향이',70,78,90)
]
sql="INSERT INTO python_student VALUES(ps_no_seq.nextval,:1,:2,:3,:4)"
for row in item:
    cursor.execute(sql,row)
conn.commit()
print("데이터 첨부 완료")
cursor.close()
conn.close()
