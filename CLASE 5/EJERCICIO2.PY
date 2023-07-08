import matplotlib.pyplot as plt
meses =[1,2,3,4,5,6,7,8,9,10,11,12]
lluvias =[134,47 ,104 ,51 ,75 ,179,75, 49 , 68, 185, 94 , 142]
plt.title("LLUVIA PCIA DE BS AS 2019")
plt.xlabel("MESES")
plt.ylabel("lluvia")
plt.bar(meses,lluvias, color="red")

plt.show()