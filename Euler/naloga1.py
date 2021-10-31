def vsota_naravnih_stevil_veckratnikov_3_5(n):
    vsota = 0
    x = 0
    while x <= n-1:
        if x % 5 == 0 or x % 3 == 0:
            vsota += x
            x += 1
        else:
            x += 1
    return vsota
print(vsota_naravnih_stevil_veckratnikov_3_5(1000))