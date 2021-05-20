class Human:
    __slots__=['name','age']  #멤버변수 고정 
    def printData(self):
        print(self.name,self.age)

h=Human()
h.name="홍길동"
h.age=20
h.printData()