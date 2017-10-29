if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(set((map(int, input().split())))))
    print("%s" % arr[-2])
    

