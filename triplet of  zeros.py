a = [-1, -2, 1, -3, 4, 5, -6, -7, 0]
b = []

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if a[i] + a[j] + a[k] == 0:
                b.append([a[i], a[j], a[k]])

print(b)
