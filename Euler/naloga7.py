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

def n_to_prastevilo(n):
    prastevila = []
    m = 0
    while len(prastevila) <= n-1:
        if je_prastevilo(m):
            prastevila.append(m)
        m += 1
    return prastevila[-1]

print(n_to_prastevilo(10001))
