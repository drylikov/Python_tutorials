principal = 1200
rate = 0.05
numyears = 5
year = 1

while year <= numyears:
    principal = principal*(1 + rate)
    print year, principal
    year += 1


