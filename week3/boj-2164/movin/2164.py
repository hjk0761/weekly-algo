from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])

def solve(q: deque):
    while q:
        top = q.popleft()
        if not q:
            return top
        top = q.popleft()
        q.append(top)

print(solve(q))