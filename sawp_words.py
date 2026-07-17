a = "i love python prog"
b = a.split()
for i in b:
    if len(i) >=2:
        b[0],b[1] = b[1],b[0]
c = (" ").join(b)
print(c)
