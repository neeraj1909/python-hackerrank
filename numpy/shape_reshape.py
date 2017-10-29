import numpy


def main():
    array = numpy.array(input().split(), int)
    print(numpy.reshape(array, (3, 3)))
    

    
if __name__ == "__main__":
    main()
