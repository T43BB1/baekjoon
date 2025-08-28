import sys
N = int(sys.stdin.readline().rstrip())
subject = list(map(int,sys.stdin.readline().rstrip().split()))
m = max(subject)
total = 0
for num in subject:
    total += int(num) / m * 100
print(total / N)