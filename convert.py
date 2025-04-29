def to_arabic(n):
    numerals = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }

    sum = 0
    last = float("inf")
    for i in range(len(n)):
        index = n[i].lower()
        sum += numerals[index]
        if numerals[index] > last:
            # Because last has already been added once
            sum -= 2 * last
        last = numerals[index]
    
    return sum

def to_roman(n):
    numerals = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
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
        val = indexes[i]
        count = n // val
        sum += count * numerals[val]
        n -= count * val
        
    return sum.upper()