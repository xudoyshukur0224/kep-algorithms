# def map(func, sequence):
#     return list(lambda x, y : x / y)
def map(func, sequence):
    lst = []
    for i in sequence:
        lst.append(func(i))

    return lst

print(map(lambda x :  x // 2, [1, 2, 3, 4]))  