import sqlite3
#1. 연결 
def studentListData():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    sql="""
          SELECT hakbun,name,kor,eng,math,
                 (kor+eng+math),ROUND((kor+eng+math)/3.0,2)
          FROM student
        """
    cur.execute(sql)
    for row in cur:
        print(row)
    cur.close()
    conn.close()

#함수 호출 
#studentListData()
def studentDetailData(hakbun):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    sql=f"""
          SELECT hakbun,name,kor,eng,math,
                 (kor+eng+math),ROUND((kor+eng+math)/3.0,2)
          FROM student
          WHERE hakbun={hakbun}
         """
    cur.execute(sql)
    data=cur.fetchone()
    for row in data:
        print(row)
    cur.close()
    conn.close()
    
#호출 
studentDetailData(7)    












