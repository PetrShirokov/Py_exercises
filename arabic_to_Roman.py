def to_roman(num):
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
