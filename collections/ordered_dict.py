from collections import OrderedDict


def main():
    n = int(input())
    ordered_dictionary = OrderedDict()
    for _ in range(n):
        item, space, price = map(str, input().rpartition(' '))
        ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)
    for item, price in ordered_dictionary.items():
        print("{0} {1}".format(item, price))
        



if __name__ == "__main__":
    main()
