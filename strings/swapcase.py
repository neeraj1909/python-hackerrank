def swap_case(s):                
    return ''.join(s.swapcase())



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
