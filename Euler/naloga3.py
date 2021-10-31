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

def prafaktorji(stevilo):
	faktorji = []
	for i in range(1, int((stevilo) ** (1 / 2)) + 1):
		if stevilo % i == 0:
			faktorji.append(i)
			faktorji.append(stevilo // i)
	return faktorji

def najvecji_prafaktor_ki_je_prastevilo(stevilo):
	najvecji_prafaktor = 0
	for faktor in prafaktorji(stevilo):
		if je_prastevilo(faktor) == True:
			if faktor > najvecji_prafaktor:
				najvecji_prafaktor = faktor
	return najvecji_prafaktor 

print(najvecji_prafaktor_ki_je_prastevilo(600851475143))
