import math

import matplotlib
import numpy as np
import numpy as numpy
from matplotlib import pyplot as plt

N = 200000

experiment1_array = list()
experiment1_values = 2

experiment2_array = list()
experiment2_values = 4

experiment3_array = list()

experiment4_array = list()

experiment5_array = list()

experiment345_values = 50


def mean_exp_4_5(x, n):
    total = 0
    for i in x:
        total += i
    return total / n


def mean_exp_1_2_3(n):
    return n / 2


def variance_1_2_3(n):
    return n / 12


def standard_deviation_1_2_3(n):
    return math.sqrt(variance_1_2_3(n))


def variance_4_5(given_array, N):
    mean = mean_exp_4_5(given_array, N)
    total = 0
    for i in given_array:
        total += (i - mean) ** 2
    return total / N


def standard_deviation_4_5(given_array, N):
    return math.sqrt(variance_4_5(given_array, N))


def gaussian_distribution(x_values, standard_deviation, mean_value):
    gauss = 1 / (standard_deviation * np.sqrt(2 * np.pi)) * np.exp(
        -(x_values - mean_value) ** 2 / (2 * standard_deviation ** 2))
    print("Mean Value:", mean_value)
    print("Standard Deviation:", standard_deviation)
    print("Variance:", standard_deviation ** 2)
    return gauss


def arange_organise(experiment_array):
    minimum = min(experiment_array)
    maximum = max(experiment_array)
    arange_ratio = (maximum - minimum) / 200
    return np.arange(minimum, maximum, arange_ratio)


def value_generator(how_many):
    total = 0
    for _ in range(how_many):
        total = total + numpy.random.uniform()
    return total


def value_generator_exp4(how_many):
    total = 0
    value = numpy.random.uniform(0, 200)
    total = total + value
    for _ in range(how_many - 1):
        if value < 99:
            value2 = numpy.random.uniform(0, 200)
            total = total + value2
            value = value2
            continue
        if value >= 99:
            value3 = numpy.random.uniform(98, 102)
            total = total + value3
            value = value3
    return total


def value_generator_exp5(how_many):
    total = 0
    for _ in range(how_many):
        a = numpy.random.uniform()
        b = numpy.random.uniform(a, 1)
        total = total + numpy.random.uniform(a, b - a)
    return total


# experiment no 1
print("EXPERIMENT 1")
print("Experiment 1 stats:")
for i in range(N):
    experiment1_array.append(value_generator(experiment1_values))
matplotlib.pyplot.hist(experiment1_array, density=True, bins=100)
array_of_x1s = arange_organise(experiment1_array)
array_of_y1s = gaussian_distribution(array_of_x1s, standard_deviation_1_2_3(experiment1_values),
                                     mean_exp_1_2_3(experiment1_values))
plt.plot(array_of_x1s, array_of_y1s)
plt.show()
print("")

# experiment no 2
print("EXPERIMENT 2")
print("Experiment 2 stats:")
for i in range(N):
    experiment2_array.append(value_generator(experiment2_values))
matplotlib.pyplot.hist(experiment2_array, density=True, bins=100)
array_of_x2s = arange_organise(experiment2_array)
array_of_y2s = gaussian_distribution(array_of_x2s, standard_deviation_1_2_3(experiment2_values),
                                     mean_exp_1_2_3(experiment2_values))
plt.plot(array_of_x2s, array_of_y2s)
plt.show()
print("")

# experiment no 3
print("EXPERIMENT 3")
print("Experiment 3 stats:")
for i in range(N):
    experiment3_array.append(value_generator(experiment345_values))
matplotlib.pyplot.hist(experiment3_array, density=True, bins=100)

array_of_x3s = arange_organise(experiment3_array)
array_of_y3s = gaussian_distribution(array_of_x3s, standard_deviation_1_2_3(experiment345_values),
                                     mean_exp_1_2_3(experiment345_values))
plt.plot(array_of_x3s, array_of_y3s)
plt.show()
print("")

# experiment no 4
print("EXPERIMENT 4")
print("Experiment 4 stats:")
for i in range(N):
    experiment4_array.append(value_generator_exp4(experiment345_values))

matplotlib.pyplot.hist(experiment4_array, density=True, bins=100)
array_of_x4s = arange_organise(experiment4_array)
array_of_y4s = gaussian_distribution(array_of_x4s, standard_deviation_4_5(experiment4_array, N),
                                     mean_exp_4_5(experiment4_array, N))
plt.plot(array_of_x4s, array_of_y4s)
plt.show()
print("")

# experiment no 5
print("EXPERIMENT 5")
print("Experiment 5 stats:")
for i in range(N):
    experiment5_array.append(value_generator_exp5(experiment345_values))
matplotlib.pyplot.hist(experiment5_array, density=True, bins=100)
array_of_x5s = arange_organise(experiment5_array)
array_of_y5s = gaussian_distribution(array_of_x5s, standard_deviation_4_5(experiment5_array, N),
                                     mean_exp_4_5(experiment5_array, N))
plt.plot(array_of_x5s, array_of_y5s)
plt.show()
