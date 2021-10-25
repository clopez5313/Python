import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm

number_of_data_points = 99
random_data_set = np.random.randn(number_of_data_points)
print(type(random_data_set))

print(random_data_set.mean())
print(np.median(random_data_set))

min_max = np.array([random_data_set.min(), random_data_set.max()])
print(min_max)

spread_measures = np.array([np.std(random_data_set), np.var(random_data_set)])
print(spread_measures)

print(sp.stats.describe(random_data_set))

iq_mean = 100
iq_std_dev = 15
iq_distribution = norm(loc=iq_mean, scale=iq_std_dev)
for n in np.arange(8):
    print('{:6.2f}'.format(iq_distribution.rvs()))

iq_pdf = iq_distribution.pdf(110)
print('{:6.2f}'.format(iq_pdf))

iq_value = 120
iq_below = iq_distribution.cdf (iq_value)
iq_above = 1 - iq_below
print('Probability that IQ is below{:4d} is {:4.2f}; probability above: {:4.2f}'.format(iq_value, iq_below, iq_above))

mu, sigma = 100, 15
data_set = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(data_set, 50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('IQ Score')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
