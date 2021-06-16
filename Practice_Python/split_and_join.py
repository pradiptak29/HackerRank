def split_and_join(line):
    # write your code here
    splited = line.split(" ")
    joined = '-'.join(splited)
    return joined


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)