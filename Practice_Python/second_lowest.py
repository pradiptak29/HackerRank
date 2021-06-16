if __name__ == '__main__':
    stu_grade=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu_grade.append([name,score])
    # print(stu_grade)
    sorted_scores = sorted(list(set([x[1] for x in stu_grade])))
    # print(sorted_scores)
    second_lowest = sorted_scores[1]

    low_final_list = []
    for stu in stu_grade:
        if second_lowest == stu[1]:
            low_final_list.append(stu[0])

    for stu in sorted(low_final_list):
        print(stu)
