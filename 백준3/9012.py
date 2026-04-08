import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    stack = []
    is_valid = True

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  
            if not stack:
                is_valid = False
                break
            stack.pop()

    if is_valid and not stack:
        print("YES")
    else:
        print("NO")
