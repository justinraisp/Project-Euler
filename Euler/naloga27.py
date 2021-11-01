
import time
import math

def je_prastevilo(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True

def funkcija():
    najvec = 0
    x, y = 0, 0
    for a in range(-1000, 1000):
        for b in range(-1000,1001):
            n = 0
            while True:
                if je_prastevilo(n**2 + a*n + b):
                    n += 1
                else:
                    if n > najvec:
                        najvec = n
                        x, y = a, b
                    break
    return int(x*y)

print(funkcija())           
