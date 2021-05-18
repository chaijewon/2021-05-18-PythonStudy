import random
'''
   연산자 
   ***1) 산술연산자 
      +,-,*,/,% => / (정수/정수=실수)
      // (정수//정수=정수) , ** (제곱)  10**2 => 10^2 => 100
      문자열+문자열(결합) 문자열+정수(X) , 문자열+실수(X)
                           str(정수)       str(실수)
   ***2) 비교연산자
      == , != , < , > , <= ,>= (결과값 : True/False)
   ***3) 논리연산자
      &&(X)=>and , ||(X) => or , !(X) => not(부정)
   4) 비트/쉬프트
      &(직렬) , |(병렬) , ^ , << , >> : 아두이노(파이썬으로 연결)
   ***5) 대입연산자
      = (치환연산자)
   ***6) 복합대입연산자
      += , -= , *= , /= , %= , **= , //=
      =======
'''
'''
# 치환연산자(대입연산자) : =
v1=3; # int v1=3
# 복수의 주소에 저장 
v1=v2=v3=5 # int v1=5,v2=5,v3=5 # int v1,v2,v3; v1=v2=v3=5
print(v1,v2,v3,end="\t") # end는 default "\n"
#여러개의 변수에 값을 대입하는 방법 
a,b=10,20 
print(f"a={a},b={b}")
c,d=b,a
print(f"c={c},d={d}")
'''
# 산술연산자 
'''
a=10
b=3
print(a+b)  #13
print(a-b)  #7
print(a*b)  #30
print(a/b)  #3.333333
print(a%b)  #1
print(a//b) #3 (정수/정수=정수)
print(a**b) #10^3

print('홍'+'길'+'동')
print('홍길동'*10)
print('홍'+str(10)) #String.valueOf()
print(bool(1),bool(-1),bool(0),bool(3)) #0이 아닌 모든 수는 True , 0일 경우만 False
print(bool(0.0),bool(0.1),bool(10.5)) #0.0이 아닌 모든 실수는 True , 0.0일 경우에만 False
print(10+int("10"))
#  산술 연산 => 데이터형 (형변환)
print(10.5+float("10.5"))
print(10.5+10)
   문자열 변환 : str(데이터형)
   정수 변환 : int(문자열)
   실수 변환 : float(문자열)
   논리형 변환 : bool(정수,실수)

# 비교연산자 (결과값 : bool)=>정수값으로 변경
# int a=10  => &a *a
a=10
b=9
print(a is b) #같은 주소의 값을 참조 
print(id(a),id(b))
print(int(a==b)) #주소에 저장된 값이 같은지 
print(a,b)
print(int(a!=b)) #True 1
print(int(a<b)) #False 0
print(int(a>b)) #True  1
print(int(a<=b)) #False  a<b or a==b 0
print(int(a>=b)) #True   a>b or a==b 1
'''
# 논리연산자 ( 조건 and 조건 ,  조건 or 조건 ) => 비교연산자 (if,for조건 , while조건)
'''
                           and         or 
    ============================================
    True True             True        True  
    ============================================
    True False           False        True  
    ============================================
    False True           False        True  
    ============================================
    False False          False        False
    ============================================
    부정 연산자 (not())
'''
a=10
b=20
c=0
# not 연산자 => bool 
print(not(a<b))
print(not(a))
print(not(b))
print(bool(c))
print(not(c))

x=10
y=9
#y+=1 #++,--(X)  y=y+1
print(x<y and x==y+1)
print(x>y and x==y+1)

print(x<y or x==y+1)
print(x>y or x==y+1)

#복합대입 연산자
'''
  a+=10  => a=a+10
  b+=5   => b=b+5
  
  문자열 , 제어문 
''' 
a=random.randrange(1,101)
#print(f"a={a}")
while(True):
    user=int(input("정수입력(1~100)"))
    if user<a:
        print(f"입력값 보다 큰값을 입력하세요")
    elif user>a:
        print(f"입력값 보다 작은값을 입력하세요")
    else:
        print(f"정답입니다")
        break

print("게임 오버!!")
       


 















