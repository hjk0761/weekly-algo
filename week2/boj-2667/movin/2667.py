n = int(input())
field = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    field[i] = list(map(int, input()))

visited = [[False for _ in range(n)] for _ in range(n)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(y, x):
    if visited[y][x]:
        return 0
    if field[y][x] == 0:
        return 0
    count = 1
    visited[y][x] = True
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        if field[ny][nx] == 0:
            continue
        if visited[ny][nx]:
            continue
        count += bfs(ny, nx)
    return count

result = []
for i in range(n):
    for j in range(n):
        size = bfs(i, j)
        if size > 0:
            result.append(size)
result.sort()
print(len(result))
for re in result:
    print(re)