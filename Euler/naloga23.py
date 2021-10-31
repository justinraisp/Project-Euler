def delitelji(n):
    delitelji1 = [1]
    for i in range(2, int(n**(1/2) + 1)):
        if n % i == 0:
            delitelji1.extend([i, n/i])
    return list(set(delitelji1))

abuntne_stevilke = []

for i in range(12, 28123):
    if sum(delitelji(i)) > i:
        abuntne_stevilke.append(i)

ne_abuntne_stevilke = [i for i in range(28123)]

for i in range(len(abuntne_stevilke)):
    for j in range(i, 28123):
        if abuntne_stevilke[i] + abuntne_stevilke[j] < 28123:
            ne_abuntne_stevilke[abuntne_stevilke[i]+abuntne_stevilke[j]] = 0
        else:
            break

print(sum(ne_abuntne_stevilke))
