from itertools import product

def maximized_value(l, m):
    """
    possible_combinations = list(product(*l))
    maximum = -1
    for x in possible_combinations:
        total = 0
        for y in x:
            total = total + (y)**2
        total = total % (m)   
        if total > maximum :
            maximum = total
    return maximum            
    """
    result = map(lambda x : sum(i**2 for i in x) % m, product(*l))
    return max(result)
                   


def main():
    k, m = map(int, input().split())
    l = (list(map(int, input().split())) [1:] for _ in range(k))
    maximum = maximized_value(l, m)
    print("{0}".format(maximum))


if __name__ == "__main__":
    main()
