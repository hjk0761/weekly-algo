s = list(input())

result = 0
count = 0
prev = ''
for c in s:
    if c == '(':
        count += 1 
        prev = c
        continue
    if prev == '(':
        count -= 1
        result += count
        prev = c
        continue
    prev = c
    result += 1
    count -= 1

print(result)