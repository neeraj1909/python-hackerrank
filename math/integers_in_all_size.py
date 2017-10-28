def calculation(a,b,c,d):
    return str(pow(a, b) + pow(c, d))

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    result = calculation(a, b, c, d)
    print("%s" % result)
    
if __name__ == "__main__":
    main()
