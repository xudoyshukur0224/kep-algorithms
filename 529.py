# map(func, iterable)
def divisors_count(son):
    count = 0
   
    for i in range(1, son + 1):
        if son % i == 0:
            count += 1 
            
    return count

def map_divisors_count(sequence):
    return map(map_divisors_count, sequence)

print(list(map_divisors_count([-8, 10, 4, 0, 12, -5]))) 

# print(map_divisors_count(10))  # 4
# print(map_divisors_count(0)) # 0
# print(map_divisors_count(-1)) # 0

