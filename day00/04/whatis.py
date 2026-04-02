import sys

def is_odd(num:int) -> bool:
    return (num % 2) == 1

try:
    if len(sys.argv) == 1:
        sys.exit(0)
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    try:
        num = int(sys.argv[1])
    except (IndexError, ValueError):
        raise AssertionError("argument is not an integer")
    if is_odd(num):
        print (f"I'm Odd")
    else:
        print (f"I'm Even")
except AssertionError as e:
    print (f"AssertionError: {e}")