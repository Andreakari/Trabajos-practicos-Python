import matplotlib.pyplot as plt
hora=[00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
temperatura=[10,9,9,8,8,8,8,8,8,8,9,10,13,14,16,16,15,13,12,12,11,11,11,11]
plt.plot(hora,temperatura)
plt.title("VARIACION DE TEMPERATURA")
plt.xlabel("HORA")
plt.ylabel("TEMPERATURA")

plt.show()
