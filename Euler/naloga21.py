def najdi_deljitelje(n):
    potencialni_deljitelj = 1
    list_deljiteljev = []
    while potencialni_deljitelj < n:
        if n % potencialni_deljitelj == 0:
            list_deljiteljev.append(potencialni_deljitelj)
        potencialni_deljitelj += 1
    return list_deljiteljev
 
def vsota_stevil():
    omejitev = 10_000
    stevilo = 1
    list_amicable_stevil = []
    while stevilo < omejitev:
        list_deljiteljev_stevila = najdi_deljitelje(stevilo)
        vsota_deljiteljev_stevila = sum(list_deljiteljev_stevila)
        list_deljiteljev_novega_stevila = najdi_deljitelje(vsota_deljiteljev_stevila)
        vsota_deljiteljev_novega_stevila = sum(list_deljiteljev_novega_stevila)
        if vsota_deljiteljev_novega_stevila == stevilo and vsota_deljiteljev_stevila < omejitev and stevilo > vsota_deljiteljev_stevila:
            list_amicable_stevil.append(stevilo)
            list_amicable_stevil.append(vsota_deljiteljev_stevila)
        stevilo += 1
    return sum(list_amicable_stevil)

print(vsota_stevil()) 