from itertools import permutations

def calculation(s, x):
    """
    for i in permutations(sorted(s), int(x)):
        print("".join(i))
    """
    print(*[''.join(i) for i in permutations(sorted(s), int(x))], sep = "\n")
 

def main():
    string , value = input().split()
    calculation(string, value)


if __name__ == "__main__":
    main()
