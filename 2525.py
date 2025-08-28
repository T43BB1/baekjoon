A, B = map(int, input().split())
C = int(input())

if B+C >= 60:
    A += (B+C) // 60
    B = (B+C) % 60
    if A > 23:
        A -= 24 
else:
    B += C

print(A, B)