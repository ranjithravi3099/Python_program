a = [1, 33, 4, 55, 66, 77, 58, 99, 91, 100, 1000]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
print(a[-1])
print(a[-2])
print(a[-3])
