# 1 + 2 + 3 + 4 + ... + n
# n = int(input())
# s = 0 
# for number in range(1, n + 1):
#     s += number

# print(s) 
import math
n = int(input())
s = 0 
for number in range(1, n + 1):
    s += int(math.sqrt(number))

print(s) 