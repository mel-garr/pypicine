import sys

def ft_filter(fofo, lop):
    for i in lop:
        if fofo is None:
            if i:
                yield i
        else :
            if fofo(i):
                yield i

    # if fofo is None:
    #     return (i for i in lop if i )
    # return (i for i in lop if fofo(i))

def main():
    # ft_filter()
    pass


if __name__ == "__main__":
    main()