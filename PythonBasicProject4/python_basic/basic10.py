# 상속 
# => web(function,class)
class Human:
    name=''
    sex=''
    age=0
    #생성자
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
    def run(self):
        pass
    def eat(self):
        pass
'''
man=Human("홍길동","남자",25)
print("나이:{},sex:{},이름:{}".format(man.age,man.sex,man.name))
man.run()
man.eat()
# print(f"나이:{man.age}....")
woman=Human("심청이","여자",20)
print("나이:{},sex:{},이름:{}".format(woman.age,woman.sex,woman.name))

파이썬 
  => 변수 ,메소드 (기본: public) : 생략을 하면 public 
  => 변수 => private 
'''
class Student(Human):
    school=''
    subject=''
    
    def __init__(self,school,subject):
        self.school=school
        self.subject=subject
    #오버라이딩 
    '''
       오버라이딩 
       1. 상속 조건 
       2. 메소드명이 동일 
       3. 매개변수가 동일
       4. 리턴형이 같다 
    '''
    def run(self):
        print("학생이 달린다")
    def eat(self):
        print("학생이 먹는다")

std=Student("SIST","파이썬")
std.name='이순신'
std.age=20
std.sex='남자'

print("이름:"+std.name)
print("학교명:"+std.school)
print("나이:"+str(std.age))
std.eat()
std.run()    
    
    
    
        