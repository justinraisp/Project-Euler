def fakulteta(n):
    if n == 1:
        return 1
    else:
        return n * fakulteta(n-1)

def vsota_stevk(n):
    if n == 0:
        return 0
    else:
        return n % 10 + vsota_stevk(n//10)

print(vsota_stevk(fakulteta(100)))