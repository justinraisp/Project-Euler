from itertools import permutations

def n_ta_permutacije_prvih_i_stevil(n, i):
    return list(permutations(range(i)))[n-1]

print(n_ta_permutacije_prvih_i_stevil(1000000,10))