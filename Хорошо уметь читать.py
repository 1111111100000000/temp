n = input()
x = []
for i in range(int(n)):
    v = input()
    if v[0:4] == '####':
        continue
    if v[0:2] == '%%':
        print(v[2:])
    else:
        print(v)
