class Singleton:
    inst=None
    def __new__(cls):
        if cls.inst is None:
            cls.inst=object.__new__(cls)
        return cls.inst
    def aa(self):
        print("임의의 메소드")

class Sub(Singleton):
    name=''
    def display(self):
        print(self.name)

s1=Sub()
s1.name="홍길동"
s2=Sub()
s2.name="심청이"

print(id(s1),id(s2))
s1.display()
s2.display()
           