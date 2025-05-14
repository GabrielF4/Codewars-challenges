bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

alphabet_to_name = {
    '01': 'bin',
    '01234567': 'oct',
    '0123456789': 'dec',
    '0123456789abcdef': 'hex',
    'abcdefghijklmnopqrstuvwxyz': 'allow',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 'allup',
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': 'alpha',    
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': 'alphanum'
}

def convert(input, source, target):
    #Bases for the input and output is the length of respective alphabets
    base_in = len(source)
    base_out = len(target)

    #Define conversion between the bases and int
    char_to_int_source = {}
    int_to_char_target = {}

    for i, character in enumerate(source):
        char_to_int_source[character] = i
    for i, character in enumerate(target):
        int_to_char_target[i] = character

    #Convert input to decimal
    value_dec = 0
    for i, character in enumerate(input[::-1]):
        value_dec += char_to_int_source[character] * pow(base_in, i)

    #Get the highest power of the base that is lower than the source value
    i = 0
    while value_dec >= pow(base_out, i + 1):
        i += 1

    #Loop through each power of the base value from i-0 and convert it to 
    return_str = ""
    while i >= 0:
        return_str += str(int_to_char_target[value_dec//pow(base_out, i)])
        value_dec %= pow(base_out, i)
        i -= 1

    return return_str


input_value = "63"
target_value = convert(input_value, dec, hex)
print(f'"{input_value}" {alphabet_to_name[dec]} -> {alphabet_to_name[hex]}: {target_value}')