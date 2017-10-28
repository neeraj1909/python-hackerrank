def calculation(a, b):
    result = divmod(a, b)
    print("%s" % (a // b))
    print("%s" % (a % b))
    print("(%s, %s)" % result)

def main():
    a = int(input())
    b = int(input())
    calculation(a, b)
    
if __name__ == "__main__":
    main()
