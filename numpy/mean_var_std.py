import numpy

def calculation(a):
    print(numpy.mean(a, axis = 1))
    print(numpy.var(a, axis = 0))
    print(numpy.std(a, axis = None))


def main():
    n, m = map(int, input().split())
    array = numpy.array([input().split() for _ in range(n)], int)
    calculation(array)


if __name__ == "__main__":
    main()
