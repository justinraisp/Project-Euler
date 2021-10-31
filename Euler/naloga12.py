def n_to_triangularno_stevilo(n):
    stevilo = 0
    a = 1
    for i in range(n):
        stevilo += a
        a += 1
    return stevilo


def prvo_triangularno_stevilo_Z_vec_kot_k_delitelji(k):
    j = 0 
    n = 0 
    stevilo_deliteljev = 0  
    while stevilo_deliteljev <= k:
        stevilo_deliteljev = 0
        j += 1
        n = n_to_triangularno_stevilo(j)

        i = 1
        while i <= n**0.5:
            if n % i == 0:
                stevilo_deliteljev += 1
            i += 1

        stevilo_deliteljev *= 2
    return n
print(prvo_triangularno_stevilo_Z_vec_kot_k_delitelji(500))