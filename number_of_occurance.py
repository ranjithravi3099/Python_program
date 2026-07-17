s = "playwright"
a = {}
for i in s:
    if i in a:
        a[i] = a[i]+1
    else:
        a[i]= 1

print(a)

for i,j in a.items():
    if a[i] <= 1:
        print(i,"-",a[i])
