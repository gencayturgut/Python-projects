from math import sqrt

import numpy as np
import numpy.random
from matplotlib import pyplot as plt

sample_size = 50000

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

for i in range(sample_size):
    U.append(np.random.uniform(0, 1))
    Xa.append(sqrt(U[i]))
    av_Xa.append(np.mean(Xa))
    vr_Xa.append(np.var(Xa))
# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i], U[i]], [1, 1.2])

plt.figure()
plt.figure()
hU = plt.hist(U, 100, alpha=0.5, density=True)
hXa = plt.hist(Xa, 100, alpha=0.5, density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))
# Plot the average and variance values.
y_axis_exp_a= []
for i in range(sample_size):
    y_axis_exp_a.append(i)

plt.figure()
plt.plot(y_axis_exp_a, av_Xa)

plt.figure()
plt.plot(y_axis_exp_a, vr_Xa)



# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []


def f(x):
    return x * 2  # pdf of F(x)=x^2


constant = 17
count = 0
while count < sample_size:
    u = np.random.rand()
    Y = np.random.rand()
    Xb.append(u)
    if (Xb[count] >= Y * constant):
        count += 1
        av_Xb.append(np.mean(Xb))
        vr_Xb.append(np.var(Xb))
    else:
        Xb.pop()

# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb, 100, density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

y_axis_exp_b = []
for i in range(sample_size):
    y_axis_exp_b .append(i)

plt.figure()
plt.plot(y_axis_exp_b , av_Xb)

plt.figure()
plt.plot(y_axis_exp_b , vr_Xb)
plt.show()
