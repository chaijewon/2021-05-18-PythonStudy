# 반복문 (while,for)
'''
   while 조건: => 조건이 True일 경우만 수행   => 반복횟수가 지정이 안된 경우
     실행문장 1
     실행문장 2
'''
# 1~10까지 출력하는 while 
# 루프변수 설정 
i=1
while i<=10:
    print("i=%d" %i)
    i=i+1
print("==============") # end="\n"
i=1
while i<=10:
    if i%2==0:
        print("i=%d" %i)
    i+=1
print("=============")
i=1
while i<=10:
    if(i%2!=0):
        print(f"i={i}")
    i+=1
print("=====누적합=======")
sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print(f"1~100까지 누적합:{sum}")

# 1~100 짝수의 합, 홀수의 합 , 전체 합
i=1
sum=odd=even=0
while i<=100:
    if i%2==0:
        even+=i
    else:
        odd+=i
    sum+=i
    i+=1
print(f"1~100까지의 짝수 합:{even}")
print(f"1~100까지의 홀수 합:{odd}")
print(f"1~100까지의 총 합:{sum}")










