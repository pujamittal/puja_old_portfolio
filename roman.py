numeral_conversion = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}


def roman(numerals):
    total = 0
    last_num = 0
    cur_num = 0
    for x in numerals[::-1]:
        cur_num = numeral_conversion[x]
        total = (total - cur_num) if (last_num > cur_num) else (total + cur_num)
        last_num = cur_num
    return total
