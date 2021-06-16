x = int(input())
y = int(input())
z = int(input())
n = int(input())

q =[]
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i + j + k != n:
                p = [i, j, k]
                # print(p)
                q.append(p)
            k += 1
        j += 1
    i += 1

print(q)
