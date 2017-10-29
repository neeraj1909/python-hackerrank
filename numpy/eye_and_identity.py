import numpy


def main():
    n , m = map(int, input().split())
    print(numpy.eye(n, m, k = 0))
    
if __name__ == "__main__":
    main()
