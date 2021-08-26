import numpy as np
import matplotlib.pyplot as plt
import DistNs3 as Dist


# params
dim = 50          # accuracy of plot. 1/dim is
randNum = 5000   # number of Random numbers to plot
size = 5 * dim

# Burr Distribution Params
# landa, c, k = 35.71, 2.09, 4.397
landa, c, k = 0.3, 8, 2


# Generate Data from the I CDF
histBurr = Dist.dataGen(dim, randNum, size, "burr", landa, c, k)

# From Python
from scipy.stats import burr12
x1 = np.linspace(burr12.ppf(0.01, c, k),
                 landa*burr12.ppf(0.99, c, k), 100)

# From ns-3
import pandas as pd
dat = np.array(pd.read_csv("RandBurr.txt"))
histBurrNs3 = np.zeros(size)
for i in range(0, len(dat)):
    rnd = dim * dat[i]
    if rnd >= size:
        continue
    histBurrNs3[int(rnd)] += 1
histBurrNs3 *= dim / len(dat)

# Plot the figure
legend_entries = []
x = np.arange(0, size / dim, 1 / dim)

# PYTHON
plt.plot(x, burr12.pdf(x/landa, c, k)/landa,
       'r-', lw=2)
legend_entries += ['Burr python']

# I-CDF
plt.bar(x, histBurr, width=0.01)
legend_entries += ["I-CDF Burr"]

# NS3
plt.bar(x, histBurrNs3, color=['green'], width=0.01)
legend_entries += ['Burr ns3']


plt.legend(legend_entries, loc='best')
plt.grid()
plt.title("Burr Dist l=0.3 c=8 k=2")
plt.xlabel('X')
plt.ylabel('PDF')
plt.savefig('BurrsDistTest-l=1 c=0.5 k=2.png')
plt.show()


