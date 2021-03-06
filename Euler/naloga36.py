def je_palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        False

def pretvori_v_binarni(n):
    return int(bin(n).replace('0b', ''))

def vsota_palindromov_do(n):
    vsota = 0
    for stevilo in range(1, n + 1):
        if je_palindrom(stevilo) and je_palindrom(pretvori_v_binarni(stevilo)):
            vsota += stevilo
    return vsota

print(vsota_palindromov_do(1000000))