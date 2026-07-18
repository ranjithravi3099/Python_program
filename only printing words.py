a = "@@he##llo$$ w%%or^?ld,."

result = ""

for ch in a:
    if ch.isalnum() or ch == " ":
        result += ch

print(result)
