def max_2(*args):
    son = list(args)
    son.sort(reverse=True)
    return son[1]  

print(max_2(2, -3, 5, 7))             