def encode(st):
    retrn_str = ""
    for c in st.lower():
        if c.isalpha():
            retrn_str += str(ord(c) - ord('a') + 1)
        else:
            retrn_str += c
            
    return retrn_str

def encode_shorted(st):
    return ''.join(str(ord(c) - ord('a') + 1) if c.isalpha() else c for c in st.lower())

print(encode_shorted("abc-def123"))