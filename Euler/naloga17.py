slovar_stevil_z_besedo = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety', 
    100 : 'onehundred',
    200 : 'twohundred',
    300 : 'threehundred', 
    400 : 'fourhundred',
    500 : 'fifehundred',
    600 : 'sixhundred',
    700 : 'sevenhundred',
    800 : 'eighthundred',
    900 : 'ninehundred',
    1000 : 'onethousand'
}

def vsota_crk_stevil_do(n):
    vsota = 0
    for stevilo in range(1, n+1):
        if stevilo in slovar_stevil_z_besedo:
            vsota += len(slovar_stevil_z_besedo[stevilo])
        elif stevilo < 100:
            besede = slovar_stevil_z_besedo[int(str(stevilo)[0]) * 10] + slovar_stevil_z_besedo[stevilo % 10]
            vsota += len(besede)
        elif stevilo < 1000:
            stotice = slovar_stevil_z_besedo[int(str(stevilo)[0]) * 100] + 'and'
            if stevilo % 100 < 20:
                ostalo = slovar_stevil_z_besedo[stevilo % 100]
            else:
                ostalo = slovar_stevil_z_besedo[int(str(stevilo)[1]) * 10] + slovar_stevil_z_besedo[stevilo % 10]
            beseda = stotice + ostalo
            vsota += len(beseda)
    return vsota

print(vsota_crk_stevil_do(1000))
