def funkcija(a,b):
    stevila_veckrat = []
    for i in range(2, a):
        for j in range(2, b):
            stevilo = i ** j
            stevila_veckrat.append(stevilo)
    stevila_enkrat = []
    for stevilo in stevila_veckrat:
        if stevilo not in stevila_enkrat:
            stevila_enkrat.append(stevilo)
    return len(stevila_enkrat)
    
print(funkcija(101,101))