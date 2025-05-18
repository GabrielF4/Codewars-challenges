def validate_base(num, base):
    numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for elem in num:
        if elem not in numbers[:base]:
            return False
    return True
   

print(validate_base('CJD70EBG65F9IHKL142A38', 22))