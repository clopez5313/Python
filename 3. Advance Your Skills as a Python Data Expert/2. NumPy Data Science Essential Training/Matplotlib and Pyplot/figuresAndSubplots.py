import numpy as np
import matplotlib.pyplot as plt


# Create the figure.
my_first_figure = plt.figure("My First Figure")

# Add two subplots to the figure.
subplot_1 = my_first_figure.add_subplot(2, 3, 1)
subplot_6 = my_first_figure.add_subplot(2, 3, 6)

# Creates a plot where the cummulative sum of each element is created.
plt.plot(np.random.rand(50).cumsum(), 'k--')
# plt.show()

subplot_2 = my_first_figure.add_subplot(2, 3, 2)

# Creates a scatter-gram.
plt.plot(np.random.rand(50), 'go')
plt.show()
