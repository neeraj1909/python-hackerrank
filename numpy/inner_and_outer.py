import numpy

def calculation(a, b):
    print(numpy.inner(a, b))
    print(numpy.outer(a, b))
    
    
def main():
    a = numpy.array(input().split(), int)
    b = numpy.array(input().split(), int)
    calculation(a, b)


if __name__ == "__main__":
    main()

