def numero(x): 
    if x >= 0:
        f=1
        for i in range(1,x+1):
            f= f * i
        return f
    else:
        return 0
n=int(input("INGRESE UN NUMERO: "))
print(f"el factorial del numero {n} es: {numero(n)}")
    
            