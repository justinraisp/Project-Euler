def dolzina_collatzovo(n):
    sez = []
    while n != 1: 
        sez.append(n)           
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return len(sez)

def vsa_zaporedja_do_stevila(stevilo):
    n = 1
    dolzina_zacetni = {}
    while n != stevilo:
        dolzina_zacetni[dolzina_collatzovo(n)] = n
        n += 1
    return dolzina_zacetni[max(dolzina_zacetni)]

print(vsa_zaporedja_do_stevila(1000000))     