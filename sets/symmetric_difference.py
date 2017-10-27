if __name__ == '__main__':
    m = int(input())
    arr1 = list(map(int, input().split()))
    n = int(input())
    arr2 = list(map(int, input().split()))
    
    arr1 = set(arr1)
    arr2 = set(arr2)
    result = list(arr1.difference(arr2)) + list(arr2.difference(arr1))
    result = sorted(result)
    for i in range(len(result)):
        print("%s" % result[i])
    
