def average_marks(sheet):
    for i in zip(*sheet):
        print(sum(i) / len(i))


def main():
    n, x = map(int, input().split())
    sheet = []
    for _ in range(x):
        sheet.append(map(float, input().split()))
    average_marks(sheet)


if __name__ == "__main__":
    main()
