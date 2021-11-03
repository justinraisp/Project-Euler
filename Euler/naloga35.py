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

def rotacije_stevila(n):
    rotacije = set()
    for i in range(len(str(n))):
        j = int(str(n)[i:] + str(n)[:i])
        rotacije.add(j)
    return rotacije

def circular_stevila_do(meja):
    stevila = []
    for i in range(meja):
        if je_prastevilo(i):
            veljavno = True
            for j in rotacije_stevila(i):
                if not je_prastevilo(j):
                    veljavno = False
                    break
            if veljavno:
                stevila.append(i)
    return stevila

print(len(circular_stevila_do(1000000)))
            