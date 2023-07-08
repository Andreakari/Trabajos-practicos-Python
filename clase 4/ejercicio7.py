def pares(numeros): 
       numeros_pares=[]
       for n in numeros:
           if n % 2==0:
              numeros_pares.append(n)
                     
       return numeros_pares
numeros=[1,2,4,6,7,8]

resultado=pares(numeros)
print(numeros)
print (resultado)
       




