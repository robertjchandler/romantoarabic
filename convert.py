def to_arabic(n):
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    sum = 0
    last = float("inf")
    for i in range(len(n)):
        index = n[i].upper()
        if index not in numerals:
            return
        sum += numerals[index]
        if numerals[index] > last:
            # Because last has already been added once
            sum -= 2 * last
        last = numerals[index]
    
    return sum

def to_roman(n):
    numerals = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    indexes = {
        0: 1000,
        1: 900,
        2: 500,
        3: 400,
        4: 100,
        5: 90,
        6: 50,
        7: 40,
        8: 10,
        9: 9,
        10: 5,
        11: 4,
        12: 1
    }

    sum = ''
    for i in range(len(indexes)):
        value = indexes[i]
        count = n // value
        sum += count * numerals[value]
        n -= count * value    
        
    return sum