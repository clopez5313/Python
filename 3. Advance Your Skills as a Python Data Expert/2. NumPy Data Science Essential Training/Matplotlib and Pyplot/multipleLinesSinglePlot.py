import numpy as np
import matplotlib.pyplot as plt


data_set_size = 15
low_mu, low_sigma = 50, 4.3
low_data_set = low_mu + low_sigma * np.random.randn(data_set_size)
high_mu, high_sigma = 57, 5.2
high_data_set = high_mu + high_sigma * np.random.randn(data_set_size)

days = list(range(1, data_set_size + 1))

plt.plot(days, low_data_set)
plt.show()

plt.plot(days, low_data_set,
         days, high_data_set)
plt.show()

plt.plot(days, low_data_set,
         days, low_data_set, "vm",
         days, high_data_set,
         days, high_data_set, "^k")
plt.show()

plt.plot(
         days, high_data_set, "^k")
plt.show()

plt.plot(days, low_data_set,
         days, low_data_set, "vm",
         days, high_data_set,
         days, high_data_set, "^k")
plt.xlabel('Day')
plt.ylabel('Temperature: degrees Farenheit')
plt.title('Randomized temperature data')
plt.show()

plt.plot(days, low_data_set,

         days, high_data_set
         )
plt.xlabel('Day')
plt.ylabel('Temperature: degrees Farenheit')
plt.title('Randomized temperature data')
plt.show()

plt.plot(
         days, high_data_set, "^k")
plt.xlabel('Day')
plt.ylabel('Temperature: degrees Farenheit')
plt.title('Randomized temperature data')
plt.show()

t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

# note that plot returns a list of lines.  The "l1, = plot" usage
# extracts the first element of the list into l1 using tuple
# unpacking.  So l1 is a Line2D instance, not a sequence of lines
l1, = plt.plot(t2, np.exp(-t2))
l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go', t1, np.log(1 + t1), '.')
l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')

plt.legend((l2, l4), ('oscillatory', 'damped'), loc='upper right', shadow=True)
plt.xlabel('time')
plt.ylabel('volts')
plt.title('Damped oscillation')
plt.show()
