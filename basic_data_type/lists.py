if __name__ == '__main__':
    N = int(input())
    
    #code starts here
    l = []
    for _ in range(N):
        x = input().split(' ')
        command = x.pop(0)
        
        if len(x) > 0:
            if command == 'insert':
                eval("l.{0} ( {1}, {2})".format(command, x[0], x[1]))
            else:
                eval("l.{0} ( {1})".format(command, x[0]))
        
        elif command == 'print':
            print(l)
        
        else:
            eval("l.{0} ()".format(command))
    
    

