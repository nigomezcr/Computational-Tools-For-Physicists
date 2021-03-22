import numpy as np
import matplotlib.pyplot as plt

datax, datay = np.loadtxt("sum.txt", unpack = True)

fig, ax = plt.subplots()
ax.plot(datax, datay, 'r-o', label="Data")
ax.legend()
ax.set_xlabel("n max")
ax.set_ylabel("|Sumup - Sumdown|")


fig.savefig("python_sum.pdf")
