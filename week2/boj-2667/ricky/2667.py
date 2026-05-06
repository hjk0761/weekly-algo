from collections import deque

n = int(input().strip())
arr = [input().strip() for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False for _ in range(n)] for _ in range(n)]

houseCount = 0
houseCountArr = []

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            if cx < 0 or cx >= n or cy < 0 or cy >= n:
                continue
            if arr[cx][cy] == '0' or visited[cx][cy]:
                continue

            queue.append((cx, cy))
            visited[cx][cy] = True
            count += 1

    houseCountArr.append(count)

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            houseCount += 1
            bfs(i, j)

houseCountArr.sort()

print(houseCount)
for count in houseCountArr:
    print(count)
