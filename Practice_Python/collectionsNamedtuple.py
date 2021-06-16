import collections

if __name__ == "__main__":
    n = int(input())
    scol = ','.join(input().split())
    Student = collections.namedtuple('Student',scol)

    sum = 0
    for i in range(n):
        row = input().split()
        student = Student(*row)
        sum += int(student.MARKS)

    print(sum/n)




# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6


# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5