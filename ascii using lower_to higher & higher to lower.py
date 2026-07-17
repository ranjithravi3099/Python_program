a = "ranjith"
b = ""

for i in range(len(a)):
    c = ord(a[i])
    d = chr(c - 32)
    b = b + d
print(b)


a = "ranjith"
b = ""

for i in range(len(a)):
    c = ord(a[i])
    d = chr(c + 32)
    b = b + d
print(b)
