def main():
    m = int(input())
    a = set(input().split())
    n = int(input())
    
    for _  in range(n):
        eval('a.{0}({1})'.format(input().split()[0], input().split()))
        
    result = sum(map(int, a))
    print("%s" % result)
    
if __name__ == '__main__':
    main()
    
    
    
        
    
