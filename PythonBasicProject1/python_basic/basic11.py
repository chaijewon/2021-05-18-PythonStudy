'''
   변수 : 변수명에는 데이터가 저장된 주소를 참조하고 있다(참조변수)
     => 주소를 출력 id(변수명)
     => 데이터형이 필요없다 
     => 변수명=값
     ==================================================
     변수형 => int , float , str , bool
     문자열 : '' , ""  => 배렬기호로 ss[0]
     집합
       => list => [값,값...] => 출력은 for
          => 데이터베이스  
     ==================================================
      데이터 처리 
        연산자 : // ** , and, or, not => 단항연산자 (++,--(X))
        제어문 : 조건문 => 다중 조건문 elif 
                반복문 => for 
'''
import cx_Oracle
class Emp:
    empno=0
    ename=''
    job=''
    hiredate=''
    sal=0.0
    dname=''
    loc=''
  
conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
cursor=conn.cursor()
sql=f"""
      SELECT empno,ename,job,hiredate,sal,dname,loc 
      FROM emp,dept
      WHERE emp.deptno=dept.deptno
     """
cursor.execute(sql)
for row in cursor:
    for i in range(len(row)):
        print(row[i],end=" ")
    print()
     







