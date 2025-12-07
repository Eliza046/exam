for a in range(1000,1,-1):
    k=0
    for x in range(1,1000):
        if (70%a==0)and((x%28==0) <= ((not(x%a==0)) <= (not(x%21==0)))):
            k+=1
    if k == 999:
        print(a)
        break