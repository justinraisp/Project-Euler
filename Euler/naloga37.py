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

def skrajsaj_stevilo(n):
    stevila = []
    n = str(n)
    for i in range(0, len(n)):
        stevila.append(int(n[i:]))
        stevila.append(int(n[:i+1]))
    
    return stevila[1:]

def so_prastevila(stevilo):
    stevila = skrajsaj_stevilo(stevilo)
    for i in stevila:
        if not je_prastevilo(i):
            return False
    return True


def funkcija37():
    stevila = []
    stevilo = 11
    while len(stevila) < 11:
        if so_prastevila(stevilo):
            stevila.append(stevilo)
        stevilo += 1
    return stevila


print(sum(funkcija37()))
