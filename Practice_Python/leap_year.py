if __name__ == '__main__':
    def is_leap(year):
        leap = False

        # Write your logic here
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        else:
            if year % 400 == 0:
                leap = True
            else:
                leap = False

        return leap


    year = int(input())
    print(is_leap(year))
