a = "hey darling how was the yesterday"
c =a.split()
b = ""
for i in c:
    if len(i) >= len(b):
        b = i
print(b)
