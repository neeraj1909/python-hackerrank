import numpy

def main():
    n , m = map(int, input().split())
    array = numpy.array([input().split() for _ in range(n)], int)
    print (array.transpose())
    print (array.flatten())
        
        
if __name__ == "__main__":
    main()