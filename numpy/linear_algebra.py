import numpy

def calculation(a):
    print(numpy.linalg.det(a))


def main():
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], float)
    calculation(a)


if __name__ == "__main__":
    main()
