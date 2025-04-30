import convert

def main():
    # 1918, the first year of the Spanish flu pandemic
    value = ("MCMXVIII", 1918)
    for i in range(len(value)):
        n = value[i] # To be replaced by user input
        t = type(n)
        if t == int:
            print(convert.to_roman(n))
        elif t == str:
            print(convert.to_arabic(n))
        else:
            return
        
main()