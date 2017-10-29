if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    #code starts here
    t = tuple(integer_list)
    print("%s" % ( hash(t)))
