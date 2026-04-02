import sys
from ft_filter import ft_filter

def main():
    # print(filter.__doc__)
    try:
        assert len(sys.argv) == 3
        text = sys.argv[1].split(" ")
        num = int(sys.argv[2])

        print(list(ft_filter(lambda ss: len(ss) > num, text)))


    except (AssertionError, ValueError):
        print(f"AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()