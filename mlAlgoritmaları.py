
def costFunc(salaryData, param1):

    #x =  salaryData["yil"].values
    #y = salaryData["maas"].values
    
    m = 33

    error = []

    for i in range(m):
        sonuc = param1*salaryData.iloc[[i], [0]]
        xiError = (sonuc - salaryData.iloc[[i], [1]])*(sonuc- salaryData.iloc[[i], [1]])
        error.append(xiError)

    costParam1 = (1/(2*m))*sum(error)
    return costParam1

#maliyet fonksiyonunu minimize eder
def gradientDescent2Param(salaryData, learnRate, nIter):

    # gradient descent'in daha hızlı hesaplanması için datayı scaleliyoruz
    X = salaryData["yil"].values
    Y = salaryData["maas"].values/10000

    # elimizde kaç örnek olduğunu buluyoruz
    m = len(X)

    # parametrelerimize bir başlangıç değeri atıyoruz
    param0 = 0
    param1 = 0

    # parametreleri maliyet lokal minimuma yaklaşana kadar güncelle
    for _ in range(nIter):

        dParam0 = []
        dParam1 = []

        #i için hata toplamı
        for i in range(m):
            dParam0.append((param0+param1*X[i])-Y[i])
            dParam1.append(((param0+param1*X[i])-Y[i])*X[i])

        # her iterasyonda parametreleri güncelliyoruz
        param0 = param0-learnRate*(1/m)*sum(dParam0)
        param1 = param1-learnRate*(1/m)*sum(dParam1)

    return param0, param1

# bulduğumuz parametreleri kullanarak lineer bir fonksiyon oluşturuyor ve inputa göre tahminimizi yapıyoruz
def tahmin(X, param0, param1):
    return (param0 + param1*X)*10000
