from itertools import product

if __name__ == "__main__":
    a = input().split(" ")
    b = input().split(" ")
    a = list(map(int, a))
    b = list(map(int, b))
    output = list(product(a,b))

    for i in output:
        print(i, end=" ")