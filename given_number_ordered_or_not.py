#number;
#_______
a = [10,20,30,40,50]
order = True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        order = False
print(order)
