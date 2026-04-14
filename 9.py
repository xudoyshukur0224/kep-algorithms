def reverse_number(number):
    string_number =  str(number)
    return int( string_number[::-1])
# print(reverse_number(1895)) # 5981
for num in range(1000, 10000):
    reverse_num =  reverse_number(num)
    if reverse_num == 4 * num:
        print(num)