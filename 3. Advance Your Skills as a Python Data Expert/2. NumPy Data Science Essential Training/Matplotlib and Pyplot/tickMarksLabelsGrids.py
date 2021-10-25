import numpy as np
import matplotlib.pyplot as plt


number_of_data_points = 1000

my_figure = plt.figure()
subplot_1 = my_figure.add_subplot(1, 1, 1)
subplot_1.plot(np.random.rand(number_of_data_points).cumsum())

number_of_ticks = 5
ticks = np.arange(0, number_of_data_points, number_of_data_points//number_of_ticks)
subplot_1.set_xticks(ticks)

labels = subplot_1.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=45, fontsize='small')

subplot_1.set_title ("My First Ticked Plot")
subplot_1.set_xlabel ("Groups")

subplot_1.grid(True)
gridlines = subplot_1.get_xgridlines() + subplot_1.get_ygridlines()
for line in gridlines:
    line.set_linestyle(':')
plt.show()
