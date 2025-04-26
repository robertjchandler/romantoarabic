def to_arabic(n):
    # The values of all single Roman numerals
    numerals = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }

    if type(n) is not str:
        return "Input must be a Roman numeral"
    elif n.lower() not in numerals:
        return "Only 'i', 'v', 'x', 'l', 'c', 'd' and 'm' are allowed in the input"
    else:
        return numerals[n.lower()]