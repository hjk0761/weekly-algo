t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    dist_sq = dx * dx + dy * dy

    sum_r_sq = (r1 + r2) * (r1 + r2)
    diff_r_sq = (r1 - r2) * (r1 - r2)

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif dist_sq > sum_r_sq:
        print(0)
    elif dist_sq == sum_r_sq:
        print(1)
    elif diff_r_sq < dist_sq < sum_r_sq:
        print(2)
    elif dist_sq == diff_r_sq:
        print(1)
    else:
        print(0)
