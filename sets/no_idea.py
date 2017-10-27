if __name__ == "__main__":
    n, m = input().split()
    arr = list(map(int, input().split()))
    set1 = set(list(map(int, input().split())))
    set2 = set(list(map(int, input().split())))
    
    happiness = 0
    for x in arr:
        if x in set1:
            happiness = happiness + 1
        if x in set2:
            happiness = happiness - 1
    print("%s" % happiness)
            
    
