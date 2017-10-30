import numpy

def calculation(a, b):
    print(numpy.dot(a, b))


def main():
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(n)], int)
    calculation(a, b)


if __name__ == "__main__":
    main()
