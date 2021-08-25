from scipy.stats import burr
import matplotlib.pyplot as plt
import numpy as np
# import tikzplotlib

c, k = 1, 1
mean, var, skew, kurt = burr.stats(c, k, moments='mvsk')

fig, ax = plt.subplots(1, 1)
legend_entries = []

# x = np.linspace(burr.ppf(0.01, c, k),
#                 burr.ppf(0.99, c, k), 100)
#
# ax.plot(burr.cdf(x, c, k),
#        'r-', lw=2, label='burr pdf')
# legend_entries += ['burr pdf']
#
# rv = burr(c, k)
# ax.plot(rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#
# legend_entries += ['frozen pdf']

r = burr.rvs(c, k, size=50)
ax.hist(r)
legend_entries += ['Rand']



plt.legend(legend_entries, loc='best')
plt.grid()
plt.xlabel('X')
plt.ylabel('PDF')
plt.show()
plt.savefig('BurrDist.png')
# tikzplotlib.save("Output/BurrDist.tex")