n = int(input())
total_guess = [str(i) for i in range(1,n+1)]
guess = list(map(str, input().split()))
while guess[0].upper() != 'HELP':
    ans = input()
    if ans.upper() == 'YES':
        for t in total_guess:
            if t not in guess:
                total_guess.remove(t)
                for t in total_guess:
                    if t not in guess:
                        total_guess.remove(t)
    elif ans.upper() == 'NO':
        for t in total_guess:
            if t in guess:
                total_guess.remove(t)
    guess = list(map(str, input().split()))
print(*total_guess)