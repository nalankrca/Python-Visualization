#setosanın SepalLengthCm de her vir valuenin firekansını ölçmek istediğimiz zaman kullanırız.Kaç adet aynı değerden var
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")

setosa=df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


plt.hist(setosa.PetalLengthCm,bins=10)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title( "histogram")
plt.show()