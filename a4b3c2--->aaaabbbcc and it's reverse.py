a = "a4b3c2a5"
c = ""

for i in range(0, len(a), 2):
    ch = a[i]
    count = int(a[i + 1])

   # for j in range(count):
    #    c = c + ch
    c = c + ch * int(count)  
        

print(c)



a = "aaabbbccc"

count = 1
result = ""

for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        count += 1
    else:
        result = result + a[i] + str(count)
        count = 1

# Add the last character and its count
result = result + a[-1] + str(count)

print(result)

