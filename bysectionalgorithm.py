x = int(input('Enter an Integer: '))
epsilon = 0.000000001
numGuess = 0
low = 0
high = x
ans = (high+low)/2
while abs(ans**2 - x) >= epsilon and ans<=x:
    numGuess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2
print('number of guesses',numGuess)
print(ans,'is the closest square root of',x)
