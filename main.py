import convert, sys

def main():
    valid_numerals = "0123456789"
    if len(sys.argv) == 3:
        # Command line arguments
        if sys.argv[1] == "-r":
            for numeral in sys.argv[2]:
                if numeral not in valid_numerals:
                    return
            print(convert.to_roman(int(sys.argv[2])))
        elif sys.argv[1] == "-a":
            print(convert.to_arabic(sys.argv[2]))
        else:
            return
    else:
        return
        
main()