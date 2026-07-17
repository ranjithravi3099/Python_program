numbers = [1, 2, 3, 4, 7]

target = 10

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Indices",i,j)
            
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Numbers",numbers[i],numbers[j])
