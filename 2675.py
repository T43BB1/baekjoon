T = int(input())

for _ in range(T):
    R, S = input().split()
    b = ""
    for a in S:
        b += int(R) * a
    print(b)


# print(, end = "") = 이어서 출력 

# T = int(input())

# for _ in range(T):
#     R, S = input().split()
#     for a in S:
#         a += int(R) * a
#         print(a, end = "")
