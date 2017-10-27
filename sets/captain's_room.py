def main():
    k = int(input())
    l = list(map(int, input().split()))

    l_set = set(l)
    captain_room_no = ((sum(l_set)*k) - sum(l)) / (k-1)
    print("%s" % int(captain_room_no))

if __name__ == "__main__":
    main()
    
