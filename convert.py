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

    sum = 0
    last = float("inf")
    for i in range(len(n)):
        index = n[i].lower()
        sum += numerals[index]
        if numerals[index] > last:
            sum -= 2 * last
        last = numerals[index]
    
    return sum