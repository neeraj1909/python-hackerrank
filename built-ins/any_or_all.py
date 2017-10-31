def main():
    n = int(input())
    l = input().split()
    print(all([int(x) > 0 for x in l]) and any([str(x) == str(x)[::-1] for x in l]))

if __name__ == "__main__":
    main()
