from matrisVektorIslemleri import *
from mlAlgoritmaları import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import test as gds

# matris vektör problemi - Bir salgında alınan verilerde 65 yaş üstü kişilerin yüzde 10'u sağlıklı, %50'si hasta, %40'ı 
# taşıyıcıdır; 65 yaş altı kişilerin %35'i sağlıklı, %30'u hasta, %35'i taşıyıcıdır. Salgından etkilenler 100 genç erkek,
# 80 yaşlı erkek, 120 genç kadın ve 100 yaşlı kadındır. Cinsiyete göre hastalıktan nasıl etkilenildiğini bulun.
#   38   40  42  44
cinsiyetYas = [
    [100, 80],
    [120, 100]
]

yasHastalık = [
    [10, 50, 40],
    [35, 30, 35]
]

sonucMatris = matrixCarp(cinsiyetYas, yasHastalık)
sonucMatris = skalerMatrisCarpim(0.01, sonucMatris)
print()
print()
print()

matrixGoster(sonucMatris)

# makine öğrenmesi problemi - Kişilerin deneyimlerine (çalışma yılı) göre aldıkları maaşı tahmin eden bir model
print()
print()
print()


salaryData = pd.read_csv("salaryData.txt", usecols = [0, 1], names = ["yil", "maas"])
#salaryData= salaryData.values.tolist()
#print(salaryData)
#costTheta= [[],[]]

#for i in range(0, 11):
 #   costY = costFunc(salaryData,float(i)/2)
 #   costTheta[0].append(float(i)/2)
 #   costTheta[1].append(costY)

#plt.plot(costTheta[0], costTheta[1])



param0, param1 = gradientDescent2Param(salaryData, 0.05, 300)
strparam0 = str(param0)
print(strparam0 + ", " )

strparam1 = str(param1)
print(strparam1 + ", " )

print(tahmin(9.6 , param0, param1))

xdAxis= []
ydAxis= []

for i in range(len(salaryData)):
    xdAxis.append(salaryData["yil"][i])
    ydAxis.append(salaryData["maas"][i])


xaAxis = np.array(xdAxis)
yaAxis = np.array(ydAxis)

plt.plot(xaAxis, yaAxis)

xcdAxis= []
ycdAxis= []

for i in range(len(salaryData)):
    xcdAxis.append(salaryData["yil"][i])
    ycdAxis.append(tahmin(salaryData["yil"][i], param0, param1))

plt.plot(xcdAxis, ycdAxis, "-r")
plt.xlabel("Maaş")
plt.ylabel("Deneyim")
plt.grid()
plt.show()
