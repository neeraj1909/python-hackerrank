import cmath

def main():
    z = complex(input())
    result = (cmath.polar(z))
    print(result[0])
    print(result[1])
    
    
if __name__ == "__main__":
    main()
