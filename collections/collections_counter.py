from collections import Counter

def income_calculation(shoes, no_of_customer):
    income = 0
    for i in range(no_of_customer):
        size, price = map(int, input().split())
        if shoes[size]:
            income = income + price
            shoes[size] = shoes[size] - 1
    return income        

def main():
    no_of_shoes = int(input())
    shoes = Counter(map(int, input().split()))
    no_of_customer = int(input())
    
    income = income_calculation(shoes, no_of_customer)
    print("{0}".format(income))
    
        
        


if __name__ == "__main__":
    main()
