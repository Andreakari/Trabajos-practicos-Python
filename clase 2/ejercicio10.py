herencia=float(input("ingrese el monto heredado:  "))
porcplazo=50 
plazofijo=float(porcplazo*herencia)/100

bonos=25
bonosinteres=float(bonos*herencia)/100
print("intereses por año de plazofijo:  ",plazofijo)
print ("inteseres de los bonos cada 6 meses:  ", bonosinteres)
if plazofijo>bonosinteres:
 print("conviene el plazo fijo por 1 año")
else:
  print("conviene el bono cada 6 meses")
  