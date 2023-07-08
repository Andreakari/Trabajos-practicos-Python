edad = int(input("INGRESE SU EDAD:   "))
if edad >=60:
    print("paga 500")
elif edad > 18:
    print("usted paga 1000")
elif edad <= 18:
    print("usted paga 400")
elif edad >= 10:
    print("usted paga 200")
elif edad  >=3:
    print("usted paga 100")
else:
    print("no paga")