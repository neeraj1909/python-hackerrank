from collections import defaultdict


def main():
    n, m = map(int,input().split())
    d = defaultdict(list)
    list1 = []
    
    for i in range(n):
        d[input()].append(i+1)
    
    for i in range(m):
        list1 = list1 + [input()]
        
    
    for i in list1:
        if i in d:
            print(" ".join(map(str, d[i])))
        else:
            print(-1)
        
    


if __name__ == "__main__":
    main()
