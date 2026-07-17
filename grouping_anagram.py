words = ["listen", "silent", "hello", "enlist", "world",
         "eat", "tea", "apple", "bat", "tab", "cat"]
         

b = {}
for i in words:
    a = "".join(sorted(i))
    if a not in b:
        b[a] = []
    b[a].append(i)
print(list(b.values()))
print(b.keys())
    
    
    
