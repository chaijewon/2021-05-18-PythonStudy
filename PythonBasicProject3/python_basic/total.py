'''
    함수 
    1. 전체 목록 출력  def select() 
    2. 상세보기       def detail(hakbun)
    3. 데이터 추가    def insert(튜플)
    4. 데이터 수정    def update(튜플) (....)
    5. 데이터 삭제    def delete(hakbun)
    6. 검색          def find(name)
'''
import cx_Oracle

def select(page):
    conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    cur=conn.cursor()
    rowSize=10
    start=(rowSize*page)-(rowSize-1)
    end=rowSize*page
    sql=f"""
         SELECT hakbun,name,kor,eng,math,total,score,rank,num 
         FROM (SELECT hakbun,name,kor,eng,math,(kor+eng+math) as total,
               ROUND((kor+eng+math)/3.0,2) as score,
               RANK() OVER(ORDER BY (kor+eng+math) DESC) as rank,rownum as num
         FROM (SELECT /*+ INDEX_ASC(python_student ps1_hakbun_pk)*/ hakbun,name,kor,eng,math 
         FROM python_student))
         WHERE num BETWEEN {start} AND {end}
        """
    #실행 
    cur.execute(sql)
    #출력 
    for row in cur:
        for std in row:
            print(std,end=" ")
        print('')
        
    #닫기
    cur.close()
    conn.close()

#함수 호출 
#page=int(input("페이지 설정:"))
#select(page)
def detail(hakbun):
    conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    cur=conn.cursor()
    sql=f"""
           SELECT hakbun,name,kor,eng,math,(kor+eng+math),
                  ROUND((kor+eng+math)/3.0,2)
           FROM python_student
           WHERE hakbun={hakbun}
         """
    cur.execute(sql)
    data=cur.fetchone() #selectOne 
    #fetchall() = selectList
    print(f"학번:{data[0]}")
    print(f"이름:{data[1]}")
    print(f"국어:{data[2]}")
    print(f"영어:{data[3]}")
    print(f"수학:{data[4]}")
    print(f"총점:{data[5]}")
    print(f"평균:{data[6]}")
    cur.close()
    conn.close()
    
#호출 
#detail(1)
#검색 
def find(name):
    conn=cx_Oracle.connect('hr/happy@localhost:1521/xe')
    cur=conn.cursor()
    sql=f"""
          SELECT * FROM recipe
          WHERE title LIKE '%{name}%'
        """
    cur.execute(sql)
    data=cur.fetchall()
    print(data)
    cur.close()
    conn.close()

#호출 
name=input("검색어 입력:")
find(name)

def delete(hakbun):
    conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    cur=conn.cursor()
    sql=f"""
          DELETE FROM python_student
          WHERE hakbun={hakbun}
         """
    cur.execute(sql)
    print("삭제 완료!!")
    conn.commit()
    cur.close()
    conn.close()
#함수 호출 
#hakbun=int(input("삭제할 학번 입력:"))
#delete(hakbun)
#select(1)
def update(data):
    #오라클 연결
    conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    cur=conn.cursor()
    sql="""
          UPDATE python_student SET
          name=:1 , kor=:2 , eng=:3 , math=:4
          WHERE hakbun=:5
        """
    cur.execute(sql,data)
    conn.commit()
    print("수정 완료")
    cur.close()
    conn.close()
    
#호출 
#update(('박문수수정',100,100,90,3))
#select(2)

def insert(data):
    conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    cur=conn.cursor()
    sql="""
         INSERT INTO python_student VALUES(
           ps_no_seq.nextval,:1,:2,:3,:4
         )
        """
    cur.execute(sql,data)
    conn.commit()
    print("추가 완료")
    cur.close()
    conn.close()
    
#호출 
#insert(('이순신님',100,100,100))
#select(2)


    
    
    
    
    
    
    
    