import matplotlib.pyplot as plt
cordoba=[16,16,16,18,18,18, 18, 23,23,23,23,23, 27,27,27,27,27,26,26,26,23, 23, 19 ]
buenosaires=[9,14, 20, 18, 18, 16, 16,16,16, 15, 15,15, 15,  12, 12, 12, 12,12,11,11,10, 10, 10,9]

plt.plot(cordoba)
plt.plot(buenosaires)
plt.title("VARIACIÓN DOS CIUDADES")
plt.xlabel("HORAS cordoba y buenos aires")
plt.ylabel("temperatura")
plt.show()
           