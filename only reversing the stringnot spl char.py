a = "ab#cd$ef"
b = []
c= ""
for i in a:
    if i.isalnum():
        b.append(i)
b.reverse()
print(b)
    
for i in a:
    if i.isalnum():
       c = c + b.pop(0)
    else:
        c = c+i
