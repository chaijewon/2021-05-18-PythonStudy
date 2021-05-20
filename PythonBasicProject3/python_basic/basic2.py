# 데이터 전체 출력 
import cx_Oracle
conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
cur=conn.cursor()
sql="SELECT /*+ INDEX_ASC(python_student ps1_hakbun_pk) */ * FROM python_student"
cur.execute(sql)
# 출력
for row in cur:
    for r in row:
        print(r,end=" ")
    print('')
