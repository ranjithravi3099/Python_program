a = "a4b3c2a5"
c = ""

for i in range(0, len(a), 2):
    ch = a[i]
    count = int(a[i + 1])

   # for j in range(count):
    #    c = c + ch
    c = c + ch * int(count)  
        

print(c)
