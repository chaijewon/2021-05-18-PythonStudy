# for : 반복문 => 횟수가 지정 
'''
  for형식 
  for 받는 변수 in 범위(리스트,튜플...) :
      실행문장 
  범위지정 (range(1,9))
'''
#print(help(print))
# sep => separator : 구분문자 (기본 " ")
# end => 마지막 문자 : (기본 "\n")
#print("a","b","c",sep=",")
# for(int i=1;i<10;i++)
for i in range(1,10): # 1~9 => 1증가
    print(f"i={i}")
print("==========")
'''
list=["red","blue","green","yellow","black","magenta","cyan"];
for color in list:
    print(color)
'''
for i in range(1,101,10): # 1~100 2씩 증가 
   print(f"i={i}")
print("===========")
for _ in range(5): #반복 수행을 5번 한다 
    print("Hello")

    
