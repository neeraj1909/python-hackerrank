import numpy

def main():
    array = tuple(map(int, input().split()))
    print(numpy.zeros((array), dtype = numpy.int))
    print(numpy.ones((array), dtype = numpy.int))

if __name__ == "__main__":
    main()
