A = int(input())
B = int(input())
C = int(input())

num="0123456789"
result = str(A*B*C)

for i in num:
    print(result.count(i))  
  
