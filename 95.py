# n = int(input())
# son = list(map(int, input().split()))

# sum = 0
# for m in son:
#     if m % 2 != 0:
#         sum += m
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# print(sum ) 

n = int(input())
s, i = 0, 0

# for i in range(n):
#     a = int(input())
#     if a % 2 == 1:
#         s += a

while i < n :
    a = int(input())
    if a % 2 == 1:
        s += a
    i += 1 
print(s)