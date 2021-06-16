if __name__ == '__main__':
    n = int(input())

    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    rounded = "{0:.2f}".format(round(avg), 1)
    print(rounded)
