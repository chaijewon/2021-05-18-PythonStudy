#상속 
'''
  class A:
  
  class B(A):
  단점 : 단일상속이 아니고 다중 상속이 가능 
  상속 : 기존에 만들아진 클래스 기능을 전체를 받아서 수정,그대로 사용
        재사용기법 
        ========
        오버라이딩 
'''
class Animal:
    def move(self):
        print("움직이는 모든 동물")

class Dog(Animal): #상속 => move()
    def eat(self):
        print("개가 먹는다")

class Pig(Animal):
    pass  #정의할 내용이 없다 (멤버가 없는 클래스 제작)

dog=Dog()
dog.move()
dog.eat()

pig=Pig()
pig.move()



