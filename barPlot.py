import numpy as np
import matplotlib.pyplot as plt

array=np.array([1,2,3,4,5,6,7,8])
x=array*2+5

plt.bar(array,x)
plt.title("Bar Plot")
plt.xlabel("Array")
plt.ylabel("transaction result")
plt.show()