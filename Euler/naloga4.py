def je_palindrom(stevilo):
    return str(stevilo) == str(stevilo)[::-1]


def najdi_najvecji_palindrom(n,m):
    najvecji = 0
    for i in range(n,m):
        for j in range(n,m):
            produkt = i*j
            if je_palindrom(produkt) and produkt > najvecji:
                najvecji = produkt
    return najvecji

print(najdi_najvecji_palindrom(100,1000))