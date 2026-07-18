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

# without using dict
a = "banana"
b = ""

for i in a:
    if i is not b:
        count = 0
        
        for j in b:
            if i ==j:
                count = count + 1
    print(i,count)
    b = b + i
