def vsota_stevk_stevila(n):
    if n == 0:
        return 0
    else:
        return n % 10 + vsota_stevk_stevila(n // 10)

print(vsota_stevk_stevila(2 ** 1000))