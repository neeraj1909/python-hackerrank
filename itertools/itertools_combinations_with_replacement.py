from itertools import combinations_with_replacement

def combination_with_replacement(s, k):
    for x in combinations_with_replacement(sorted(s), int(k)):
        print("".join(x))


def main():
    s, k = input().split()
    combination_with_replacement(s, k)


if __name__ == "__main__":
    main()
