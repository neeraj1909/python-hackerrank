import numpy

def calculation(a, b):
    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(a//b) #here I used floor division beause required solution is not obtained using "numpy.divide(a, b)"
    print(numpy.mod(a, b))
    print(numpy.power(a, b))
    
    
def main():
    n, m = map(int, input().split())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(n)], int)
    calculation(a, b)
    
    
if __name__ == "__main__":
    main()
    
    
    
