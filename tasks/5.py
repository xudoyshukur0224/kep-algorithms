lst =  [18, 22, 5, 38, 0, 7] 
s = 0
for n in lst:
    if n < 30 and n % 3 == 0:
        print(n, end=" ")
    else:
        s += n
    
print()
print(s)

