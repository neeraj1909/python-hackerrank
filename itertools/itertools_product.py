from itertools import product 

def calculation(a, b):
    #result = list(product(a,b))
    #print(" ".join(map(str, result)))
    print(*product(a, b))


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    calculation(a, b)


if __name__ == "__main__":
    main()
