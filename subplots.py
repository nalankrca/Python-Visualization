import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")
df1=df.drop(["Id"],axis=1)
setosa=df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


df1.plot(grid=True,alpha=0.9,subplots=True)
plt.show()


plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="Setosa")
plt.ylabel("Setosa-PetalLengthCm")

plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")
plt.ylabel("versicolor-PetalLengthCm")
plt.show()