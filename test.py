li = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    li.append((x, y))

for i, j in li:
    print(i, j)