nums = [0, 1, 0, 3, 12]

result1 = []
result2 = []
for i in nums:
    if i == 0:
        result1.append(i)
    else:
        result2.append(i)
print(result2 + result1)
