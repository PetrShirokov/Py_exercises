def hamming_weight(num):

    '''Counts sum of symbols in binary representation of the decimal num
    that are different from the zero-symbol.'''
    
    if num == 0:
        return 0
    weight = 0
    while num:
        weight += num % 2
    #    print('weight =', weight)
        num = num // 2
    #    print('num =', num)
    return weight

def hamming_weight_2(num):
    bin_num = bin(num)[2:]
    return bin_num.count('1')

print(hamming_weight(0)) # 0
print(hamming_weight(4)) # 1
print(hamming_weight(101)) # 4

print(hamming_weight_2(0)) # 0
print(hamming_weight_2(4)) # 1
print(hamming_weight_2(101)) # 4