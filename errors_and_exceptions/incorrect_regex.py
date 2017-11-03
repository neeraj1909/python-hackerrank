import re

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        try:
            re.compile(s)
            is_valid = True     
        except re.error:
            is_valid = False
        print(is_valid)
    

if __name__ == "__main__":
    main()
