cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibonacci_list =[0,1]
    for i in range(2,n):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    return fibonacci_list[0:n]   



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
