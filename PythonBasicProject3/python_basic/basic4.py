# 삭제 
import cx_Oracle
conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
cursor=conn.cursor() #getConnection()
sql="SELECT COUNT(*) FROM python_student"
cursor.execute(sql)
count=cursor.fetchone() #총갯수를 읽기
print(count[0])
cursor.close() #disConnection()

hakbun=int(input(f"1~{count} 중에 삭제할 번호를 선택하세요"))
sql=f"DELETE FROM python_student WHERE hakbun={hakbun}"
cursor=conn.cursor() 
cursor.execute(sql)
conn.commit()
print(f"{hakbun}삭제 완료")
cursor.close()
conn.close()