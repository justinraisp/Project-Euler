def najdi_dolzino_cikla(n):
    dolzina_cikla = 0 
    list_preostankov = []
    x = 1
    while True:
        if x % n == 0:
            break
        elif x in list_preostankov:
            break
        list_preostankov.append(x)
        x = (x * 10) % n 
        dolzina_cikla += 1
    return dolzina_cikla
     

def funkcija(d):
    dolzina_najdaljsega_cikla = 0
    i_ki_ga_iscemo = False
    for i in range(1, d):
        trenutni_cikel = najdi_dolzino_cikla(i)
        if trenutni_cikel > dolzina_najdaljsega_cikla:
            dolzina_najdaljsega_cikla = trenutni_cikel
            i_ki_ga_iscemo = i
    return i_ki_ga_iscemo

print(funkcija(1000))