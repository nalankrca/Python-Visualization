import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")

setosa=df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label=  "setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label=  "versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label=  "virginica")

plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()