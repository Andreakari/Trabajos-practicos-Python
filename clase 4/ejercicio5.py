lista=[]
print("ingrese cantidad de numeros: ")
numero=int(input())
i=0
while i < numero:
    print("valor del numero: " ,i+1)
    val=float(input())
    lista.append(val)
    i+=1
promedio=sum(lista)/len(lista)
print("el promedio es: ",promedio)
