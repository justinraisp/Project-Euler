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

def naslednje_prastevilo(n):
    n += 1
    while True:
        if je_prastevilo(n):
            return n
        n += 1

def vsota_prastevil_do_stevila_n(n):
    prastevilo = 2
    seznam_prastevil = []
    while prastevilo <= n:
        seznam_prastevil.append(prastevilo)
        prastevilo = naslednje_prastevilo(prastevilo)
    return sum(seznam_prastevil)

print(vsota_prastevil_do_stevila_n(2000000))