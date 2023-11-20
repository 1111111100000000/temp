a = input()
b = []
for i in a:
    b.append(len(i))
print(a[b.index(max(b))])