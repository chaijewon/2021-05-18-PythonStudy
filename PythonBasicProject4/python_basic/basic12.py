# 다중 상속 , 추상클래스 => 예외처리 , 파일 입출력 
# JSON파싱 , HTMLParser , Network
# 다중 상속 => 상속시 생성자는 상속되지 않는다(속도가 늦기때문에 존재한다) 
class A:
  #멤버변수 선언 
  a=''
  def aprint(self):
      self.a="한개"
      print("A생성자 호출")

class B:
  b=''
  def bprint(self):
      self.b="두개"
      print("B생성자 호출")

class C:
   c=''
   def cprint(self):
       self.c="세개"
       print("C생성자 호출")

class D(A,B,C):
    def __init__(self):
        print("D생성자 호출")
    def display(self):
        self.aprint()
        self.cprint()
        self.bprint()
        print(self.a)
        print(self.b)
        print(self.c)
        
d=D()
d.display()


