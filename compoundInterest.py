#!/usr/bin/env python3

principalAmount = 10000
annualInterest = .14

numYears = int(input('Enter number of years to calculate Compound interest: '))

finalAmount = principalAmount * ((1 + annualInterest/12) ** (numYears * 12))

print('Final amount after', numYears, 'years, is',finalAmount)
