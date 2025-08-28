N = int(input())
nums = input().strip()
total = 0   
for digit in nums: 
    total += int(digit)
print(total)