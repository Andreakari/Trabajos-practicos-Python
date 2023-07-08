print("RECETAS DEL PANADERO")
harina=int(input("ingrese cantidad de kilos de harina:    "))
azucar=int(input("ingrese cantidad de kilos de azucar:   "))
manteca=int(input("ingrese la cantidad de manteca:        "))
lista1=[harina,azucar,manteca]
lista2=[5,2,1]
if lista1==lista2:
    print("puede preparar la receta")
else:
    print("no puede preparar la receta")