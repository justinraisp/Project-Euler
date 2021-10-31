def tocke_po_crkah(ime):
    abeceda = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    tocke = 0
    for i in ime:
        stevec = 1
        for j in abeceda:
            if j == i:
                tocke += stevec
            else:
                stevec += 1 
    return tocke

def skupna_vsota():
    with open("names.txt") as f:
        datoteka_z_imeni = f
        imena = []
        for ime in datoteka_z_imeni:
            imena.append(ime)
    list = imena[0].split(',')
    urejen_list = sorted(list)
    vsota_tock = 0
    stevec = 1
    for ime in urejen_list: 
        vsota_tock += stevec * tocke_po_crkah(ime)
        stevec += 1
    return vsota_tock
   
print(skupna_vsota())