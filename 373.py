# n = int(input())
# son = list(map(int, input().split()))
# katta = max(n)
# print(katta)


n = int(input( ))

son = list(map(int, input().split()))
max_son = n[0]

for i in range(1, len(n)):
    if n[i] > max_son:
        max_son = n[i] 

print( max_son) 
