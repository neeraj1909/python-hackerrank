from math import atan2, degrees

def calculation(ab, bc):
    angle= str(int(round(degrees(atan2(ab, bc))))) + '°'
    return angle
    
    
    


def main():
    ab = int(input())
    bc = int(input())
    angle = calculation(ab, bc)
    print("%s" % angle)
    
if __name__ == "__main__":
    main()
    
