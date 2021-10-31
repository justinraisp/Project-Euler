def fibonnacijeva_stevila(n):
    stevila = [1,1]
    i = 2
    while len(str(stevila[-1])) < n:
        stevila.append(stevila[-1] + stevila[-2])
        i += 1
    return i

print(fibonnacijeva_stevila(1000))