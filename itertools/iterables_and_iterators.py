from itertools import combinations

def probability_calculation_of_k(l, k):
    count  = 0
    combination = list(combinations(l, k))
    result = filter(lambda c : 'a' in c, combination)
    print("{0:.3}".format(len(list(result))/len(combination)))
    
    
def main():
    n = int(input())
    l = input().split()
    k = int(input())
    probability_calculation_of_k(l, k)

if __name__ == "__main__":
    main()
