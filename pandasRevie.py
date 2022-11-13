import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("iris.csv")

print(df.head())
print("--")

df1= df.drop(["Id"],axis=1)