if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    
    result = len(set(arr))
    print("%s" % result)
