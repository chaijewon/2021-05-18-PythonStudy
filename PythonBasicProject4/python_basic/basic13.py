# 추상클래스 : 미완성된 클래스 => pass
# 상속을 받는 경우 => 반드시 메소드를 구현해서 사용 
from abc import *
# 추상 클래스 선언 : 구현이 안된 메소드 , 구현된 메소드가 존재 : 여러개의 클래스가 있는 경우 모아서 관리할 목적 
class Board(metaclass=ABCMeta):
    @abstractmethod
    def write(self): #구현이 안된 메소드 
        pass 
    @abstractmethod
    def detail(self): #구현된 메소드
        pass
    @abstractmethod
    def update(self): #구현된 메소드
        pass
    @abstractmethod
    def delete(self): #구현된 메소드
        pass
    @abstractmethod
    def find(self): #구현된 메소드
        pass
    

class FreeBoard(Board):
    def write(self):
        print("자유게시판 글쓰기")
    
    def detail(self):
        print("자유게시판 상세보기")
    
    def update(self):
        print("자유게시판 수정")
        
    def delete(self):
        print("자유 게시판 삭제")
        
    def find(self):
        print("자유게시판 찾기")

fb=FreeBoard()
fb.detail()
fb.write()
fb.update()
fb.delete()
fb.find()