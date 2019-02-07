import math
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 8, 12, 13]
y = [1, 3, 3, 5, 4, 10, 13]

def std(data):
    sum = 0
    for x in data:
        sum += (x - mean(data))**2
    variance = sum / len(data)
    return math.sqrt(variance)

sx = std(x)
sy = std(y)

def corr(x, y):
    sum = 0
    for i, j in zip(x,y):
        sum += ((i - mean(x)) / sx) * ((j - mean(y)) / sy)
    return 1 / len(x) * sum

r = corr(x,y)
m = r * (sy / sx)
b = mean(y) - (m * mean(x))

plt.scatter(x, y)
x_p = np.linspace(-5, 15, 100)
y_p = m * x_p + b
plt.plot(x_p, y_p, '-r')
plt.grid()
plt.show()
