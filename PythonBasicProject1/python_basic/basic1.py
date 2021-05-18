# 변수와 출력 방법 
# 변수 선언
'''
  =======   참조형   ========= (자바 :배열 , 클래스)
   1000번지  =====>    100
  =======          =========
    a                1000번지
''' 
a=100
#출력 
print(a)
# a는 10이다
# 옵션 (다른 데이터형 연결) %d(정수형) , %f(실수형) , %s(문자형) 
print("a는 %d이다" %a)
b=10
c=20.0
d="홍길동"
print("b=%d,c=%f,d=%s" %(b,c,d))
print("b:{},c:{},d:{}".format(b,c,d))
print(f"b는 {b} , c는 {c} d는 {d}") 
# sql=f"SELECT * FROM emp WHERE empno={empno}"
print(id(b),id(c),id(d))
a1=3
b1=3
# 같은 값을 가지고 있는 변수는 주소값이 같다
print(id(a1),id(b1))
print(a1 is b1)
b1=5
print(a1 is b1)
c1="Hello"
print("c1:%s" %c1,end="Python\n")
# end => \t , \n 
# end , sep (구분자)
print("a:%d" %a, "b:%f" %b, "c:%s" %c,sep="-")








