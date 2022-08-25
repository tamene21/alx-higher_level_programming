#!/usr/bin/python3
if __name__ == "__main__":
    from calculate_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    o = sys.argv[2]
    b = int(sys.argv[3])

elif o is '+':
    print("{} {} {} = {}".format(a, o, b, add(a, b)))
elif o is '-':
    print("{} {} {} = {}".format(a, o, b, sub(a, b)))
elif o is '*':
    print("{} {} {} = {}".format(a, o, b, mul(a, b)))
elif o is '/':
    print("{} {} {} = {}".format(a, o, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
