#najvecje stevilo kaj lahko dosezemo s peto potenco je 6*9**5, stevila z vec stevkami ne moremo zapisat
def funckija30():
    vsota = 0
    meja = 6*9**5
    for i in range(2, meja +1):
        vsota_potenc = 0
        for x in str(i):
            vsota_potenc += int(x)**5
        if vsota_potenc == i:
            vsota += i
    return vsota

print(funckija30())