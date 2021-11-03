#najvecje stevilo kaj gre zapisat je 7 * 9!
from math import factorial
def funkcija34():
    stevila = []
    meja = 7 * factorial(9)
    for i in range(3, meja + 1):
        vsota = 0
        for j in str(i):
            vsota += factorial(int(j))
        if vsota == i:
            stevila.append(vsota)
    return sum(stevila)

print(funkcija34())