#주석 (한줄 주석)
'''
   여러줄 주석 
   데이터형이 존재하지 않는다 (자동인식)
   변수 
   변수명=값
   a=10
   
   파이썬 
   1) 특화 (주로 사용처)
      = 빅데이터 프로그램 (라이브러리 = 데이터 수집,통계 (R))
      = 네트워크 , 인터넷(프레임워크 : Django)
      = 웹 => Database 
      = 아나콘다,판다스 => AI
   2) 웹 사이트 (기본 : Spring(Java)-backand , 
      front-end(Ajax(Jquery),VueJs,React,NodeJs))
        + 지능형 웹(검색,추천) = 파이썬 
   3) 일반 프로그램 언어
      C/C++
      Java
      Kotlin(안드로이드),스칼라 (JVM)
                                                     컴파일
      ============================  원시소스(프로그래머) ======> .class (.obj) =====> 실행
                                                                         인터프리터 
      Python : 컴파일이 없이 인터프리터 (속도 빠르다),배우기 쉽게, 데이터형이 존재하지 않고 
               설정된 변수가 메모리 공간의 이름
               모든 데이터를 객체인식을 한다 (int,float..) : 주소를 기억하고 있다   
               
      1. 변수 
      2. 연산자 
      3. 제어문 
      ===============================
      4. 함수 
      ===============================
      5. 라이브러리 
      6. 클래스(객체지향) => DTO,VO
      ===============================
      7. 데이터베이스 
      8. 웹 (장고) : 게시판 , 목록 , 상세보기 , 어드민페이지
      
      => 자료형(데이터형) , 기본문법 
      자료형 (자바: 정수형,실수형,문자형,논리형,참조형(배열,클래스))
      파이썬의 자료형 
      1. 기본 자료형 
         => 정수 
         => 실수 
         => 문자열
         => 논리형 
          <class 'int'>
          <class 'float'>
          <class 'bool'>
          <class 'str'>
      2. 집합 자료형  
         리스트형 : 중복데이터를 허용한다 , 값을 변경할 수 있다 => []
         ================================================== List,ArrayList
         튜플형 : 데이터베이스 출력 , 중복데이터 허용 , 한번 정한 값은 변경 할 수 없다 => ()
         셀형 : 중복데이터를 허용하지 않는다 => {}
         ================================================== Set
         딕트형 : 키와 값으로 표현 ["key":"value]
         ================================================== Map
      3. 함수지향언어 + 객체 지향언어 
      4. 변수 => 출력 
      ==================================================
         데이터 저장 ====== 데이터 처리  ====== 데이터 출력
                       제어문 , 연산자 
                       ===========함수
      ================================================== 클래스
      
      1.변수 (변경할 수 있다: 메모리에 저장 => 휘발성(RAM) => 프로그램이 종료되면 자동으로 삭제)
            => 영구적인 저장 장치 (파일,RDBMS(오라클,My-SQL,Sqlite(소형))
            => 자바,C,C++ 차이점 
               파이썬에서 변수는 저장할 값 자체를 기억하지 않고 객체의 주소를 기억하고 있다 (모든 변수가 참조형 기억주소)
      2. 식별자 
        = 알파벳으로 시작한다 (한글 사용이 가능 : 비권장)
        = 대소문자를 구분 
        = 숫자를 사용 할 수 있다 (단 뒤에만 사용) a1,a2...
        = 키워드는 사용할 없다 ( if , else , for , while , True...) else if => elif
          10/3  10//3 => 3  **
          ==== 3.3333
          ******* 들여쓰기
      3. 변수선언 
         변수명=값 or 다른 변수명 or 함수
         a=10
         b=20
         a="홍길동"
         b=Ture/Fasle
         c=10.5
         => 주소값을 출력 (id(변수명)) , 데이터형(type(변수명)) => 데이터베이스 연결 
'''
a=10
print(type(a))
print(id(a))
b=10.5
print(type(b))
c=True; # True , False
print(type(c))
d="Python"
print(type(d))
print(d+str(a))
print(float(a))
print(bool(1)) #bool(1) => True, bool(0) => False

for i in range(1,10):
    print(i)










