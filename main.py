import convert, sys

def main():
    valid_numerals = "0123456789"
    help = """
    "Usage:
      main.py [options] <input>

     Converts roman numerals to arabic numerals and vice versa.

     Options:
      -h, --help             display this help
      -r, --roman            convert an arabic numeral to a roman numeral
      -a, --arabic           convert a roman numeral to an arabic numeral
    """
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print(help)
        elif len(sys.argv) == 3:
            # Command line arguments
            if sys.argv[1] == "-r" or sys.argv[1] == "--roman":
                for numeral in sys.argv[2]:
                    if numeral not in valid_numerals:
                        return
                print(convert.to_roman(int(sys.argv[2])))
            elif sys.argv[1] == "-a" or sys.argv[1] == "--arabic":
                print(convert.to_arabic(sys.argv[2]))
            else:
                return
        else:
            return
    else:
        return
        
main()