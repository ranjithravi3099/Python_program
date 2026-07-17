a = ["ranjith", "kumar","good", "boy"]
b = "aeiou"

for i in a:
    count = 0
    for j in i:
        if j in b :
            count = count + 1
    
    if count >1:
        print(count,"-",i)
