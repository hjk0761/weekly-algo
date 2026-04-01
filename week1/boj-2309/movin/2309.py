height = []

for _ in range(9):
    height.append(int(input()))

height.sort()
s = sum(height)

def solve():
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            if s - (height[i] + height[j]) == 100:
                return i, j
    return -1, -1

x, y = solve()

for k in range(9):
    if k == x or k == y:
        continue
    print(height[k])