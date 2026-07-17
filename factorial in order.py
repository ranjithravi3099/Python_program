num = 10

for i in range(0,num+1):  # for i in range(num,0,-1)-----> decresing order
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    print(i, fact)
