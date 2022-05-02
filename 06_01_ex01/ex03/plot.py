# plot.py
# drawing various graphs using matplotlib
# 2022-14673 강준서

import matplotlib.pyplot as plt
import math


plt.plot([1, 2, 3], [4, 7, 2])
plt.plot([1, 2, 3], [3, 6, 4])
plt.show()

#
# plot y = x**2
# xmin < x < xmax
# n: number of intervals

xmin = -200
xmax = 300
xs = []
ys = []
n = 200000


def f(x):
    return 3*x**3 - x**2 + 3*x + 1


for i in range(0, n+1):
    x = xmin + (xmax-xmin) * i/n
    y = f(x)
    xs.append(x)
    ys.append(y)

plt.plot(xs, ys)
plt.show()



#
# circle
#

# x**2 + y**2 = 1
# y = math.sqrt(1-x**2)
# 0 <= x <=  2pi
# x = cost, y = sint


for j in range(1, 4):
    xs = []
    ys = []
    n = j*10
    for i in range(0, n + 1):
        t = 2 * math.pi * i / n
        x = math.cos(t)
        y = math.sin(t)
        xs.append(x)
        ys.append(y)

    plt.plot(xs, ys)
    plt.show()



def draw(function, interval=100, domain=(-3, 3)):
    xs = []
    ys = []
    for j in range(0, interval+1):
        x = domain[0] + (domain[1]-domain[0]) * j / interval
        y = function(x)
        xs.append(x)
        ys.append(y)
    return xs, ys


def draw_as_par(function, interval=100):
    xs = []
    ys = []
    for j in range(0, interval+1):
        t = 2 * math.pi * j / interval
        x = function(t, 0)
        y = function(t, 1)
        xs.append(x)
        ys.append(y)
    return xs, ys


def norm_dis(x):
    sd = 1
    m = 0
    return (1/math.sqrt(2*math.pi*sd**2))*math.exp(
        -1*(x-m)**2/2*sd**2
    )


def heart(t, r):
    if r == 0:
        return 16*(math.sin(t))**3
    else:
        return 13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t)


global BMI


def height_on_bmi(x):
    return math.sqrt(x/BMI)


plt.plot(*draw(norm_dis))
plt.show()

plt.plot(*draw_as_par(heart))
plt.show()

l = [18.5, 25, 30, 35, 40]
for b in l:
    BMI = b
    plt.plot(*draw(height_on_bmi, domain=(20, 120)))
plt.show()
