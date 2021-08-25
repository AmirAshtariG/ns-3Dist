import numpy as np
import matplotlib.pyplot as plt
import DistNs3 as Dist


# params
dim = 10          # accuracy of plot. 1/dim is
randNum = 5000   # number of Random numbers to plot
size = 50 * dim

# Burr Distribution Params
landa, c, k = 1/0.028, 2.09, 4.397


# Generate Data from the I CDF
histBurr = Dist.dataGen(dim, randNum, size, "burr", landa, c, k)
histBurr2 = Dist.dataGen(dim, randNum, size, "burr", 1, c, k)


from scipy.stats import burr12
# histBurrScipy = burr.rvs(c, k, size=100)
x1 = np.linspace(burr12.ppf(0.01, c, k),
                 landa*burr12.ppf(0.99, c, k), 100)


# Plot the figure
legend_entries = []
x = np.arange(0, size / dim, 1 / dim)


plt.bar(x, histBurr)
legend_entries += ["I-CDF Burr"]

plt.plot(x1, burr12.pdf(x1/landa, c, k)/landa,
       'r-', lw=2, label='burr12 pdf')
# plt.hist(histBurrScipy/100, lw=2)
legend_entries += ['Burr']

plt.legend(legend_entries, loc='best')
plt.grid()
plt.title("Burr Dist l=1/0.028 c=2.09 k=4.397")
plt.xlabel('X')
plt.ylabel('PDF')
plt.savefig('BurrsDistTest-l=0.028 c=2.09 k=4.397.png')
plt.show()


