def je_deljivo_s_stevili_do_dvajset(stevilo):
    for i in range(2, 21):
        if stevilo % i != 0:
            return False
    return True

n = 20
while True:
	if je_deljivo_s_stevili_do_dvajset(n):
		break
	n += 20
print(n)
