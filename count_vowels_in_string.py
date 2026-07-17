a1 = "aaeeeezzzz"
a= a1.lower()
b = "aeiou"
count = 0

for ch in a:
    if ch in b:
        count += 1

print(count)
