n = int(input())
l = input()
s = []
value = []
for _ in range(n):
    value.append(int(input()))

operator = ['+', '-', '*', '/']

def do(first, second, operator):
    if operator == '+':
        return first + second
    if operator == '-':
        return first - second
    if operator == '*':
        return first * second
    return first / second

def find(c, value):
    return value[ord(c) - 65]

for c in l:
    if c in operator:
        second = float(s.pop())
        first = float(s.pop())
        s.append(do(first, second, c))
    else:
        s.append(find(c, value))

print('%.2f'%s[0])
