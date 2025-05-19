def all_nines(x):
    if x % 2 == 0 or x % 5 == 0:
        return -1
    
    for i in range(1, 4000):
        num_str = str('9' * i)
        num = int(num_str)
        if num % x == 0:
            return num // x
    
    return -1

print(all_nines(243))