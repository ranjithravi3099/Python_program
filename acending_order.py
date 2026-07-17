a = [1, 33, 4, 55, 66, 77, 58, 99, 91, 100, 1000]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] < a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
