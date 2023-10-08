def to_roman(num):
    'Convert arabic num into roman_str.'
    a_to_R = {
    0: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    1: ['', 'X','XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    2: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    3: ['', 'M', 'MM', 'MMM']
}
    num_list = list(str(num))
    num_list.reverse()
    roman = ''
    for index, unit in enumerate(num_list):
        roman = a_to_R[index][int(unit)] + roman
    return roman


def to_arabic(roman_str):
    'Convert roman num in arabic. If roman num is incorrect, return False.'
    R_to_a = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    arabic_num = 0
    roman_lst = list(roman_str)
    while roman_lst:
        if len(roman_lst) == 1:
            arabic_num += R_to_a[roman_lst[0]]
            if to_roman(arabic_num) != roman_str:
                return False
            return arabic_num
        guess_num = "".join(roman_lst[:2])
        if guess_num in R_to_a:
            arabic_num += R_to_a[guess_num]
            roman_lst.pop(0)
            roman_lst.pop(0)
        else:
            current_num = roman_lst.pop(0)
            arabic_num += R_to_a[current_num]
    return arabic_num



print(to_arabic('XXI'))
print(to_roman(22))