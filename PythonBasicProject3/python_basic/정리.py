'''
   함수 정리 
   1) 재사용 기법 
   2) 한개의 기능만 수행이 가능하게 한다
   3) 명령문을 모듈화 
      = 함수 모듈화 =====> C 
      = 클래스 모듈화 ====> Java(C++)
      = 함수 + 클래스 ====> 파이썬 
      = 프론트 (Front) => 데이터를 관리 
        함수  : Vue.js , Jquery , JavaScript
        클래스 : React.js (Hooks=함수기반)
        ===> 변경 (MVC => Vuex , Redux)
   4) 데이터 관리 (데이터저장 : 변수,배열,클래스,파일,RDBMS) 
   5) 함수 종류 
      = 사용자 정의 , 라이브러리
        =========
        함수 : 사용자 요청값 (매개변수), 처리 결과값(리턴형)
        ===========================================
                리턴형        사용자 요청값(매개변수)
        ===========================================
                 O                 O
                 =>로그인 (사용자 요청:id,pwd) => 결과값을 받아서 화면변경
                 def login(id,pwd):
                    로그인 처리 
                    return 결과값
        ===========================================
                 O                 X
                 => 게시판 전체목록 
                 def boardListData():
                    처리 (데이터베이스 연결)
                    return 게시판 전체목록 
        ===========================================
                 X                 O  
                 => insert,update,delete
                 def insert(튜플):
                    insert 처리 
                 def update(튜플):
                    update 처리
                 def delete(no):
                    delete처리 
        ===========================================
                 X                 X
                 => 구구단 출력 , 정렬
        ===========================================
        사용자가 요청한 데이터가 몇개인지 모른다 : 가변매개변수  *args ( ... )
             def display(*args):
                 처리 
        default 매개변수 : 항상 뒤에서부터 설정
          def display(a=10,b,c) => display(,10,20)(오류) (X)
          def display(a,b=10,c) => (X)
          def display(a,b,c=100)=>(O)
          def display(a,b=100,c=200)=>(O)
          def display(a=100,b=200,c=300)=>(0)
          print(value,sep=" ",end="\n")
          print("aaa")
'''







