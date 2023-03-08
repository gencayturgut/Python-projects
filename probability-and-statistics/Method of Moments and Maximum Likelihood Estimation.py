from math import sqrt
import matplotlib.pyplot as plt
import np as np
import math
import numpy as np
import numpy.random

X = [0.3, 0.6, 0.9, 0.8]
N = [1, 2, 3, 4, 5, 10, 50, 100, 500, 1000]
population = 10000000


def f(x_):
    return (2 * 2.4 ** 2) / (x_ ** 3)


def mean(list_):
    total = 0
    for k in list_:
        total += k
    mean_value = total / len(list_)
    return mean_value


def variance(list_, mean_value):
    var = 0
    for j in list_:
        var += (j - mean_value) ** 2
    return var / len(list_)


def standard_deviation(list_, mean_value):
    return sqrt(variance(list_, mean_value))


def mom_estimation_for_sample_set(samples):
    samples_mean = mean(samples)
    result = samples_mean / 2
    return result


def mle_for_sample_set(samples):
    return min(samples)


def inverse_function(u):
    return math.sqrt((2.4 ** 2) / (1 - u))


def B():
    sample_set = []
    for _ in range(0, population):
        sample_set.append(inverse_function(np.random.uniform(0, 1)))
    return sample_set


def c_plot(mom_, mle_, n):
    plt.figure()
    plt.hist(mom_, bins=np.linspace(0, 4.8, 100), alpha=0.5,
             label="MOM estimate histogram for N = " + str(n))
    plt.hist(mle_, bins=np.linspace(0, 4.8, 100), alpha=0.5,
             label="MLE estimate histogram for N = " + str(n))
    plt.legend(loc='upper right')
    plt.show()


def c_print(mom_, mle_, n):
    print("For N = " + str(n) + ":")
    print(
        "MoM estimate mean: " + str(mean(mom_)) + "    MoM estimate standard deviation: " + str(
            np.std(mom_)))
    print(
        "MLE estimate mean: " + str(mean(mle_)) + "    MLE estimate standard deviation: " + str(
            np.std(mle_)))


def C(population_array, n):
    mom_array = []
    mle_array = []
    samples = []
    for _ in range(100000):  # 100000
        n_array = []
        for __ in range(n):
            n_array.append(population_array[np.random.randint(0, population)])
        mom_array.append(mom_estimation_for_sample_set(n_array))
        mle_array.append(mle_for_sample_set(n_array))
        samples.append(n_array)
    c_print(mom_array, mle_array, n)
    c_plot(mom_array, mle_array, n)


# PART A
x_estimation = mom_estimation_for_sample_set(X)
x_mle_est = mle_for_sample_set(X)
print("MoM estimate for the sample is " + str(x_estimation))
print("MLE estimate for the sample is " + str(x_mle_est))
# PART B
sample_array = B()
plt.figure()
x = np.linspace(2.5, 20.0, 100)
plt.plot(x, f(x), color="blue", label="PDF")
plt.hist(sample_array, bins=np.linspace(2.5, 20.0, 100),
         label="Histogram", density=True,
         color="orange")
plt.legend(loc='upper right')
plt.show()
# PART C
for i in N:
    C(sample_array, i)
