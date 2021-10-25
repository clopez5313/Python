import numpy as np
import matplotlib.pyplot as plt


number_of_data_points = 10

my_figure = plt.figure()
subplot_1 = my_figure.add_subplot(1, 1, 1)
subplot_1.plot(np.random.rand(number_of_data_points).cumsum())

subplot_1.text (1, 0.5, r'an equation: $E=mc^2$', fontsize=18, color='red')
subplot_1.text (1, 1.5, "Hello, Mountain Climbing!", family='monospace', fontsize=14, color='green')

# see: http://matplotlib.org/users/transforms_tutorial.html
# transform=subplot_1.transAxes; entire axis between zero and one
subplot_1.text(0.5, 0.5, "We are centered, now", transform=subplot_1.transAxes)

subplot_1.annotate('shoot arrow', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='red', shrink=0.05))

plt.show()

x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

plt.show()

x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform_point((xdata, ydata))

bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle = "->",
    connectionstyle = "angle,angleA=0,angleB=90,rad=10")

offset = 72
ax.annotate('data = (%.1f, %.1f)'%(xdata, ydata),
            (xdata, ydata), xytext=(-2*offset, offset), textcoords='offset points',
            bbox=bbox, arrowprops=arrowprops)


disp = ax.annotate('display = (%.1f, %.1f)'%(xdisplay, ydisplay),
            (xdisplay, ydisplay), xytext=(0.5*offset, -offset),
            xycoords='figure pixels',
            textcoords='offset points',
            bbox=bbox, arrowprops=arrowprops)


plt.show()

fig = plt.figure()
for i, label in enumerate(('A', 'B', 'C', 'D')):
    ax = fig.add_subplot(2,2,i+1)
    ax.text(0.05, 0.95, label, transform=ax.transAxes,
      fontsize=16, fontweight='bold', va='top')

plt.show()
