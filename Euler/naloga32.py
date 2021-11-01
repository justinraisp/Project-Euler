def je_pandigital(n, i=9):
    return len(n) == i and set(n) == set('123456789')


#ce je i enomestno stevilo, potem je j 4mestno da dobimo 4 mestno stevilo
#ce je i dvomestno stevilo, potem je j 3mestno stevilo da dobimo 4mestno stevilo
#ce nadaljujemo, se nam stvari ponovijo

def funkcija32():
    stevila = set()
    for i in range(9):
        for j in range(999, 9999):
            if je_pandigital(str(i) + str(j) + str(i*j), 9):
                stevila.add(i*j)
            elif len(str(i) + str(j) + str(i*j)) > 9:
                break
    for i in range(9,99):
        for j in range(99, 999):
            if je_pandigital(str(i) + str(j) + str(i*j), 9):
                stevila.add(i*j)
            elif len(str(i) + str(j) + str(i*j)) > 9:
                break
    return stevila
print(funkcija32())
print(sum(funkcija32()))
