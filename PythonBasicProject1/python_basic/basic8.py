# for 응용 
# 1~100까지 합을 구한다 
sum=0
even=0
odd=0
for i in range(1,101):
    if i%2==0:
        even+=i
    else:
        odd+=i
    sum+=i
    i=i+1
print("1~100까지의 합:%d" %sum)
print("1~100까지의 짝수합:%d" %even)
print("1~100까지의 홀수합:%d" %odd)