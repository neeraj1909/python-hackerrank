def subscription_calculation(arr1, arr2):
    result = arr1.union(arr2)
    return len(result)

def main():
    n = int(input())
    arr1 = set(map(int, input().split()))
    
    b = int(input())
    arr2 = set(map(int, input().split()))
    
    print("%s" % subscription_calculation(arr1, arr2))
    

if __name__ == "__main__":
    main()
    
    

    
    
    
    
    
    
