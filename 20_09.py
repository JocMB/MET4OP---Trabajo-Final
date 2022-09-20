def es_primo(num) :
    for i in range(2,num//2):
        #print(i, num)
        if num % i == 0:
            return False
    return True 

def elPrimoMil():
    n = 1
    contadorPrimos = 0

    while(True):
        if es_primo(n):
            contadorPrimos += 1
            n += 1
        else : 
            n += 1
        if contadorPrimos == 1000:
            print( n-1 )
            break
elPrimoMil()