word = input()
total = 0

for c in word:
    if c.islower():
        total += ord(c) - ord('a') + 1
    else:
        total += ord(c) - ord('A') + 27

is_prime = True
if total < 2:
    is_prime = False
else:
    for i in range(2, int(total**0.5) + 1):
        if total % i == 0:
            is_prime = False
            break

if is_prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
