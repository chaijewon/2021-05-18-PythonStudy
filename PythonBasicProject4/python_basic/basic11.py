# 멤버변수 => private 속성 (캡슐화) : 데이터는 접근 금지,메소드를 통해서 접근 (setter/getter)
'''
    name='' public 
    __name='' private
    _name='' protected
'''
import python_basic
from _overlapped import NULL
from python_basic.basic10 import Human
class Sawon:
    __sabun=0  # public 
    __name=''
    __dept=''  #부서
    __job=''   #직위

class Member:
    sa=NULL
    def __init__(self):
        self.sa=Sawon()
    def __display(self):
        self.sa.__dept="영업부"
        print("부서:"+self.sa.__dept)

mem=Member()
mem.sa.__name="홍길동"
print(mem.sa.__name)
# AttributeError: 'Member' object has no attribute 'display' 접근이 불가능할때 나타나는 에러
mem.display()
'''
sa=Sawon()
sa.__dept="영업부"
print(sa.__dept)
'''