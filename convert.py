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
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    indexes = {
        0: 1000,
        1: 500,
        2: 100,
        3: 50,
        4: 10,
        5: 5,
        6: 1
    }

    sum = ''
    for i in range(len(indexes)):
        val = indexes[i]
        count = n // val
        sum += count * numerals[val]
        n -= count * val
        
    return sum