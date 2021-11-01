#x1 + 2x2 +5x3 + 10x4 + 20x5 + 50x6 + 100x7 + 200x8 = 200
def stevilo_nacinov():
    stevilo = 1
    for x7 in range(int(200/100 + 1)):
        for x6 in range(int((200-x7*100)/50 + 1)):
            for x5 in range(int((200-x7*100-x6*50)/ 20 + 1)):
                for x4 in range(int((200-x7*100-x6*50-x5*20)/ 10 + 1)):
                        for x3 in range(int((200-x7*100-x6*50-x5*20-x4*10)/ 5 + 1)):
                            for x2 in range(int((200-x7*100-x6*50-x5*20-x4*10-x3*5)/2  + 1)): 
                                stevilo += 1
    return stevilo   
print(stevilo_nacinov())              