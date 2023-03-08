from random import randint
from matplotlib import pyplot as plt


def possibility_quantity(dice_quantity_):
    return 6 ** dice_quantity_


def possibility_quantity_p2(dice_quantity_):
    return 6 ** dice_quantity_ - 3 ** dice_quantity_


def possibility_quantity_p3(dice_quantity_):
    return 3 * dice_quantity_ * 3 ** (dice_quantity_ - 1)


def possibility1_without3(dice_quantity_):
    opposite_possibilities_p1 = 5 ** dice_quantity_
    return possibility_quantity(dice_quantity_) - opposite_possibilities_p1


def possibility1(dice_quantity_):
    possibility = possibility1_without3(dice_quantity_) / possibility_quantity(dice_quantity_)
    return possibility * 100


def possibility2(dice_quantity_):
    total = 0
    comb = 1
    combination_helper = dice_quantity_  # using this for the need in combination
    combination_multiplier = dice_quantity_
    for i in range(1, dice_quantity_):
        combination_helper = combination_helper - 1
        comb = i * comb
        total = total + (combination_multiplier / comb) * 2 ** combination_helper
        combination_multiplier = combination_multiplier * combination_helper
    possibility = (possibility1_without3(dice_quantity_) - total - 1) * 100 / possibility_quantity_p2(
        dice_quantity_)
    return possibility


def possibility3(dice_quantity_):
    total = 0
    comb = 1
    combination_multiplier = dice_quantity_
    combination_helper_1 = dice_quantity_ - 1  # using this for the need in combination
    combination_helper_2 = dice_quantity_ - 1  # using this for the need in combination
    for i in range(1, dice_quantity_):
        combination_helper_1 = combination_helper_1 - 1
        comb = i * comb
        total = total + combination_helper_2 * 3 * (combination_multiplier / comb * 2 ** combination_helper_1)
        combination_multiplier = combination_multiplier * (combination_helper_1 + 1)
        combination_helper_2 = combination_helper_2 - 1
    possibility = (total / possibility_quantity_p3(dice_quantity_)) * 100
    return possibility


def create_dices(dice_quantity_):
    dices_ = []
    for d in range(dice_quantity_):
        dice = randint(1, 6)
        dices_.append(dice)
    return dices_


def check_threes(dices_):
    how_many_threes = 0
    for dice in dices_:
        if dice == 3:
            how_many_threes = how_many_threes + 1
    if how_many_threes > 0:
        return True
    else:
        return False


def check_even_dices_p2(dices_):
    how_many_evens = 0
    for dice in dices_:
        if dice % 2 == 0:
            how_many_evens = how_many_evens + 1
    if how_many_evens > 0:
        return True
    else:
        return False


def check_even_dices_p3(dices_):
    how_many_evens = 0
    for dice in dices_:
        if dice % 2 == 0:
            how_many_evens = how_many_evens + 1
    if how_many_evens == 1:
        return True
    else:
        return False


def plot_(empirical, theoretical, n_):
    plt.xlabel("Times tried")
    plt.ylabel("Accuracy as %")
    plt.plot(n_, empirical)
    plt.plot(n_, theoretical)
    plt.xscale("log")
    plt.show()


dice_quantity = 5
N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
possibility_theoretical_p1 = []
possibilities_empirical_p1 = []
possibility_theoretical_p2 = []
possibilities_empirical_p2 = []
possibility_theoretical_p3 = []
possibilities_empirical_p3 = []

# P1
# I subtract the possibilities which doesn't include 3's from all possibilities.

theoretical_possibility1 = possibility1(dice_quantity)
print("P1 Theoretical probability:%" + str(theoretical_possibility1) + "\n")

for i in range(len(N)):
    possibility_theoretical_p1.append(theoretical_possibility1)

for n in N:
    total_threes_empirical = 0
    for _ in range(n):
        dices = create_dices(dice_quantity)
        if check_threes(dices):
            total_threes_empirical = total_threes_empirical + 1
    possibilities_empirical_p1.append(total_threes_empirical / n * 100)
    print("Trying for " + str(n) + " times:%" + str(total_threes_empirical / n * 100))
plot_(possibilities_empirical_p1, possibility_theoretical_p1, N)

# P2
# With the help from the solution from P1, I subtract the possibilities which doesn't include
# any even number from P1 and divide it into the possibilities which include evens for sure.


theoretical_possibility2 = possibility2(dice_quantity)
print("\n" + "P2 Theoretical probability:%" + str(theoretical_possibility2) + "\n")

for i in range(len(N)):
    possibility_theoretical_p2.append(theoretical_possibility2)

for n in N:
    total_threes_evens_empirical = 0
    for _ in range(n):
        dices = create_dices(dice_quantity)
        while not check_even_dices_p2(dices):
            dices = create_dices(dice_quantity)
        if check_threes(dices):
            total_threes_evens_empirical = total_threes_evens_empirical + 1
    possibilities_empirical_p2.append(total_threes_evens_empirical / n * 100)
    print("Trying for " + str(n) + " times:%" + str(total_threes_evens_empirical / n * 100))

plot_(possibilities_empirical_p1, possibility_theoretical_p1, N)

# P3
# I find the total occurrence of the dices must have 3's for sure and just for one time an even number.
# Then, I divide it into possibilities which only have an even number for once.

theoretical_possibility3 = possibility3(dice_quantity)
print("\n" + "P3 Theoretical probability:%" + str(theoretical_possibility3) + "\n")

for i in range(len(N)):
    possibility_theoretical_p3.append(theoretical_possibility3)

for n in N:
    total_threes_one_even_empirical = 0
    for _ in range(n):
        dices = create_dices(dice_quantity)
        while not check_even_dices_p3(dices):
            dices = create_dices(dice_quantity)
        if check_threes(dices) and check_even_dices_p3(dices):
            total_threes_one_even_empirical = total_threes_one_even_empirical + 1
    possibilities_empirical_p3.append(total_threes_one_even_empirical / n * 100)
    print("Trying for " + str(n) + " times:%" + str(total_threes_one_even_empirical / n * 100))

plot_(possibilities_empirical_p3, possibility_theoretical_p3, N)
