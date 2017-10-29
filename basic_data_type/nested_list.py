if __name__ == '__main__':
    student_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data.append([name, score])
    
    second_lowest = sorted(list(set([score for name, score in student_data]))) [1]
    
    """
    for name, score in sorted(student_data):
        if score == second_lowest:
            print("%s" % name)
   
    """
    print("\n".join([x for x, y in sorted(student_data) if y == second_lowest]))
    
