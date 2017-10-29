import numpy

def calculation(a):
    print(numpy.prod(numpy.sum(a, axis = 0)))


def main():
    n, m = map(int, input().split())
    array = numpy.array([input().split() for _ in range(n)], int)
    calculation(array)
    
    
    
if __name__ == "__main__":
    main()

