def main():
    a = set(map(int, input().split()))
    n = int(input())
    count = 0
    for _ in range(n):
        x = set(map(int, input().split())) 
        if (len(x.intersection(a)) == len(x) and len(a) > len(x)):
            count = count + 1
    if count == n:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
