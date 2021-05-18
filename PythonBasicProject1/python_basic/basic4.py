'''
   변수 설정 : 변수명=값  (일반 데이터형을 사용하지 않는다) => 값이 저장되어 있는 주소를 기억을 한다(모든 변수사 참조형)
             설정된 변수는 메모리 주소를 가지고 있다 
   연산자 : 형변환   정수(int),실수(float),문자열(str)
           // , ** 
           &&=>and , ||=>or , ! => not
   제어문 
     1) 조건문 
        1. 단일 조건문 
           if 조건문 :  => if (조건문) :  if 조건문 :
             실행문장
             실행문장
        2. 선택 조건문
            if 조건문 :
               실행문장  => True일때 수행하는 문장 
            else :
               실행문장  => False일때 수행하는 문장 
        3. 다중 조건문 
            if 조건문 :
               실행문장 
            elif 조건문 :
               실행문장 
            elif 조건문 :
               실행문장 
            else :
               실행문장 
     2) 반복문 
        1. while
        2. for
     3) 반복제어문 
        1. break
        2. continue
        
    => 데이터 모아서 관리 , 명령문을 모아서 관리 ==> 함수  
       ==============
       [], {},     {"":""},()  ==> 자료구조 
       == == set   ======  ==
       list          map   tuple
      ========================================== 클래스 
'''
import random
# 조건문 
#rand=random.randrange(1,101) #1~100사이의 난수 발생 
'''
print(f"난수값={rand}") => SQL => ? 

if (rand%2==0):
   print(f"{rand}는(은) 짝수입니다")
print("프로그램 종료") #if 소속문장이 아니다 

print("난수값은 %d" %rand)

if rand%2==0:
    print("%d는 짝수입니다" %rand)
else:
    print("%d는 홀수입니다" %rand)

#다중 조건문 
if rand>=90:
    print("A학점")
elif rand>=80:
    print("B학점")
elif rand>=70:
    print("C학점")
elif rand>=60:
    print("D학점")
else:
    print("F학점")
    
    
#if => 항상 수행
if rand%2==0:
    print("if문 수행")
    print("%d는 짝수" %rand)
else:
    print("else문장 수행")
    print("%d는 홀수" %rand)
    
#중첩 if : 들여쓰기 

   if 
    if

#변수 설정 

money=1000
age=25
if money>=500:
    item="사과"
    if(age<=30):
        msg="new"
    else:
        msg="old"

print(item,msg)
'''
com=random.randrange(0,3)
#print("컴퓨터 난수:%d" %com)
user=int(input("0(가위),1(바위),2(보) 가위바위보:"))

if com==0:
    print("컴퓨터:가위")
    if user==0:
        print("사용자:가위")
        print("비겼다!!")
    elif user==1:
        print("사용자:바위")
        print("사용자 Win!!")
    elif user==2:
        print("사용자:보")
        print("컴퓨터 Win!!")
if com==1:
    print("컴퓨터:바위")
    if user==0:
        print("사용자:가위")
        print("컴퓨터 Win!!")
    elif user==1:
        print("사용자:바위")
        print("비겼다!!")
    elif user==2:
        print("사용자:보")
        print("사용자 Win!!")
if com==2:
    print("컴퓨터:보")
    if user==0:
        print("사용자:가위")
        print("사용자 Win!!")
    elif user==1:
        print("사용자:바위")
        print("컴퓨터 Win!!")
    elif user==2:
        print("사용자:보")
        print("비겼다!!")



        










