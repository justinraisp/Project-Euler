def vsota_sodih_clenov_fibonaccija_do_stevila(n):
    vsota = 0
    a = 1
    b = 2
    while a <= n:
        if a % 2 == 0:
            vsota += a
        a, b = b, a + b
        
    return vsota

print(vsota_sodih_clenov_fibonaccija_do_stevila(4000000))




