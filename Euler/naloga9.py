def ali_je_pitagorejska_trojka(a, b, c):
    return a**2 + b**2 == c**2

def pitagorejska_trojka_z_vsoto_n(n):
    for c in range(n):
        for b in range(c):
            for a in range(b):
                if a+ b + c == n:
                    if ali_je_pitagorejska_trojka(a,b,c):
                        return a, b, c

x,y,z = pitagorejska_trojka_z_vsoto_n(1000)
print( x*y*z)