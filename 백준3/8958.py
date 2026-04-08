n = int(input())

for _ in range(n):
    s = input()
    score = 0
    total = 0
    
    for ch in s:
        if ch == "O":
            score += 1
            total += score
        else:
            score = 0
    
    print(total)
