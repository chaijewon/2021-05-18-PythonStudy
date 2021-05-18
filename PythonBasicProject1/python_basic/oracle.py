import cx_Oracle
con=cx_Oracle.connect('hr/happy@localhost:1521/XE')
cur=con.cursor();
#ename=input("검색어 입력:")
empno=input("사번 입력:")
#sql=f"SELECT * FROM emp WHERE ename LIKE '%{ename}%'"
sql=f"SELECT * FROM emp WHERE empno={empno}"
cur.execute(sql)
for row in cur:
    print(row)
cur.close();
con.close()