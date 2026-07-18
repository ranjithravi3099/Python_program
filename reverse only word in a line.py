a = "hello world i am tester"
c = a.split()
target = "world"
b = ""
for i in c:
    if i == target:
        b = b + i[::-1] + " "
    else:
        b = b + i + " "
print(b)
