def calculation(a, b, m):
    x = pow(a, b)
    y = pow(a, b, m)
    print("%s" % x)
    print("%s" % y)


def main():
    a = int(input())
    b = int(input())
    m = int(input())
    calculation(a, b, m)
    
if __name__ == "__main__":
    main()
