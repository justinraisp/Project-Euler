def razlika(n):
    return kvadrat_vsote(n) - vsota_kvadratov(n)

def kvadrat_vsote(n):
    vsota = 0
    for i in range(n+1):
        vsota += i
    return vsota ** 2

def vsota_kvadratov(n):
    vsota = 0
    for i in range(n+1):
        vsota += i**2
    return vsota

print(razlika(100))