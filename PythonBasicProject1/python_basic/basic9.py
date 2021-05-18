# 자료 구조 관련 => for을 응용 (오라클 연결)
'''
  1. 문자열 형 
     1) 문자들을 표한 할 수 있는 자료형 
     2) ' ', " " 사이에 들어가 있는 문자들 
        "Hello Python" , 'Hello Python'
         123456789101112
     3) index번호 0번부터 시작
     4) 중간의 일부를 수정할 수 없다 (원본은 그대로 유지) 
'''
'''
msg='Hello Python'
msg1="안녕 파이썬"
print(msg)
print(msg1)
print(msg[0]) #H
# 슬라이싱 
for s in msg:
    print(s,end="") #end가 없는 경우 \n
print('',end="\n")
ss="홍길동입니다"
print(ss)

for i in range(1,10):
    for j in range(2,10):
        print(f"{j}*{i}={j*i}",end="\t")
    print('')
'''
ss='ABCDEFGHIJ'
'''
    substring
    ABCDEFGHIJ
    0123456789
    ==========
        -3-2-1
'''
# 문자열중에 원하는 데이터만 추출 
# 문자열 자체는 for으로 출력할 수 있다 
print(f"ss={ss}") #전체 출력 
print(f"ss[0]={ss[0]}") #처음 문자를 가지고 올때
print(f"ss[-1]={ss[-1]}") #마지막 문자를 가지고 올때
print(f"ss[0:3]={ss[0:3]}") #처음부터 3글자를 가지고 온다 
print(f"ss[1:]={ss[1:]}") #두번째 문자부터 나머지 전체를 출력 
print(f"ss[-3:-1]={ss[-3:-1]}") 
print(f"ss[0:3]={ss[0:3:2]}") # 0,1,2 => AC
print(f"ss[:]={ss[:]}") #전체 
# 문자열의 주요 함수 
# 파이썬을 이용한 웹에 필요한 기능 (장고) ==> (장고 <==> 스프링) 연결 융합  ===> Vue.js,Ajax
# 챗봇(미정)
'''
  변환 
   = upper : 대문자 변환
   = lower : 소문자 변환
'''
data=" Hello Python "
print(data.upper())
print(data.lower())
#data=data.upper()
print(data.rstrip()) #right(오른쪽만 공백 제거) => trim()
print(data.lstrip()) #left (왼쪽 공백 제거)
print(data.strip()) #왼쪽 , 오른쪽 공백 제거 
print(data.swapcase()) # 소문자 = 대문자 , 대문자 = 소문자  hELLO pYTHON
print(data.__len__())
print(len(data))     #문자의 갯수 
print(data.startswith(" He")) #시작하는 문자열 => 검색(자동완성기)
print(data.find('l')) # 첫번째 나오는 문자의 위치값 
print(data.count('o')) #문자열중에 지정한 문자가 몇개 
print(data.split(" ")) #단어를 분리
print(data.index('e')) #indexOf
print(data)
# list => 배열 
# tuple => ()













