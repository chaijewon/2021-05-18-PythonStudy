# list => ArrayList(자바) => 기본 (배열)
# [] => 중복된 데이터 허용 , index번호를 가지고 있다 (순서)
# 예)  nums=[1,2,3,4,5,6...]
#      names=["","","","",""] => for 
#      오라클 데이터 연습 => 함수
names=["홍길동","심청이","춘향이","박문수","이순신"]
#출력 => 
print(names)
'''
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4]) 
for name in names:
    print(name)
'''
print(f"인원:{len(names)}") #len(names) 리스트의 갯수 (size())
# 추가 
names.append("강감찬") #마지막에 추가 ==> add(Object) 
names.insert(1,"김두한") #지정된 위치에 추가 add(int index,Object)
#출력 
print(names)
# 삭제
names.remove("심청이")
print(names) 
names.extend(["김유신","을지문덕"]) #여러개를 동시에 등록 
print(names) 
#names.reverse()
names.sort(reverse=True)
print(names)

num=[3,5,1,2,4]
print(num)
num.sort(reverse=False) #reverse : 역순으로 출력 
# reverse=False : ASC , reverse=True : DESC
print(num)

strs=["12","45","123","34","78"]
print(strs)
strs.sort()
print(strs)
