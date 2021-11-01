import fractions

def funkcija33():
    produkt = 1
    for i in range(10,100):
        for j in range(i+1, 100):
            skupne_stevke = list(set(str(i))&set(str(j)))
            if len(skupne_stevke) != 0:
                if skupne_stevke[0] != '0':
                    stevec = list(str(i))
                    imenovalec = list(str(j))
                    stevec.remove(skupne_stevke[0])
                    imenovalec.remove(skupne_stevke[0])
                    if stevec[0] != '0' and imenovalec[0] != '0':
                        if (fractions.Fraction(int(stevec[0]), int(imenovalec[0]))) == fractions.Fraction(i,j):
                            produkt *= fractions.Fraction(i,j)
    return produkt

print(funkcija33().denominator)
