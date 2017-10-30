import numpy

def calculation(p, x):
    print(numpy.polyval(p,x))


def main():
    p = numpy.array(input().split(), float)
    x = float(input())
    calculation(p, x)


if __name__ == "__main__":
    main()
