def vsota_diagonal(dim_matrike):
    clen = 1
    vsota = 1
    preskoci = 2
    while clen < dim_matrike ** 2:
        for _ in range(4):
            clen += preskoci
            vsota += clen
        preskoci += 2
    return vsota

print(vsota_diagonal(1001))