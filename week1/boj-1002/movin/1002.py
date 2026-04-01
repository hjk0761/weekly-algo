t = int(input())
result = []
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    if (x1 == x2 and y1 == y2):
        if r1 != r2:
            result.append(0)
        else:
            result.append(-1)
        continue
    dist = (x1 - x2)**2 + (y1 - y2)**2
    if dist == (r1-r2)**2 or dist == (r1+r2)**2:
        result.append(1)
    elif dist > (r1+r2)**2 or dist < (r1-r2)**2:
        result.append(0)
    else:
        result.append(2)
for re in result:
    print(re)
    