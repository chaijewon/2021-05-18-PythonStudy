'''
    1. 사용법 
       = 함수 기반 
         def 함수(): 독립 함수 
            ==
            ==
            ==
       = 클래스 기반 
         class 클래스명:
            함수 집합 
            def a(self):
            def b(self):
              기능이 없는 경우 pass
              
        = 상속 
          class A:
             def display(self):
                pass
          class B(A):
              def display(self): 상속받은 메소드 
        = 추상클래스 
          form abc import *
          class A(metaclass=ABCMeta):
             @abstrectmethod
             def aaa(self): // 구현이 안된 메소드
                pass
                
             def bbb(self): // 구현이 된 메소드
                pass
                
          class B(A):
             def aaa(self): // 구현이 안된 메소드
                pass
       
'''