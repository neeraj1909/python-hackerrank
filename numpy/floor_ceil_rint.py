import numpy

def calculation(a):
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))


def main():
    array = numpy.array(input().split(), float)
    calculation(array)
    
    
if __name__ == "__main__":
    main()
