n = int(input())
switch = list(map(int, input().split()))
m = int(input())

def toggle(index):
    if switch[index] == 0:
        switch[index] = 1
        return
    switch[index] = 0

def solve(gender, switch_number):
    idx = switch_number-1
    if gender == 1:
        while idx < n:
            toggle(idx)
            idx += switch_number
        return
    toggle(idx)
    for i in range(1, n):
        if idx-i < 0 or idx+i >= n:
            break
        if switch[idx-i] != switch[idx+i]:
            break
        toggle(idx-i)
        toggle(idx+i)
    return

for _ in range(m):
    g, s = map(int, input().split())
    solve(g, s)

result = []
for i in range(n):
    if i % 20 == 0:
        result.append([])
    result[-1].append(switch[i])

for re in result:
    print(*re)