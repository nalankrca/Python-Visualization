import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")

df1=df.drop(["Id"],axis=1) # Id sütünü silindi
df1.plot()
plt.show()

setosa=df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="Setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color="red",label="virginica")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()