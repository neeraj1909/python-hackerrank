from itertools import combinations

def calculation(s, k):
    for i in range(1, int(k) + 1):
        for j in combinations(sorted(s), int(i)):
            print("".join(j))


def main():
    s, k = input().split()
    calculation(s, k)


if __name__ == "__main__":
    main()
