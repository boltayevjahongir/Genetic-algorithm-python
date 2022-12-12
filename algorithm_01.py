import time
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random

matplotlib.use("tkagg")


x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
EPOCH = 1000
POPULATION_SIZE = 100


def draw_graph_input(x, y):
    X, Y = np.meshgrid(x, y)
    Z = X / (X ** 2 + 2 * Y ** 2 + 1)
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X', fontweight='bold')
    ax.set_ylabel('Y', fontweight='bold')
    ax.set_zlabel('Z', fontweight='bold')
    ax.plot_surface(X, Y, Z)
    plt.show()


def draw_graph(*arg):
    for item in arg:
        plt.plot(item, label=f"Qiymat-{arg.index(item) + 1}")
        plt.legend()
        font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
        # font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
        plt.title("Genitik algoritm", fontdict=font1)
        plt.grid(color='white', linestyle='--', linewidth=0.1)
    plt.show()


def population(x, y, n):
    return np.random.choice(x, n).tolist(), np.random.choice(y, n).tolist()



def crossover(x, y):
    y.reverse()
    return x, y



def new_population(x, y, x_old, y_old):

    x_new = x[:50]
    y_new = y[:50]
    x_new, y_new = crossover(x_new, y_new)
    x_passiv = x[51:]
    y_passiv = y[51:]
    x_new+=random.sample(x_passiv, 10)+np.random.choice(x_old, size=40).tolist()
    y_new+=random.sample(y_passiv, 10)+np.random.choice(y_old, size=40).tolist()
    return x_new, y_new


def fitnes(x, y):
    fit, x_new, y_new = [], [], []
    for x_item, y_item in zip(x, y):
        fit.append(x_item / (x_item ** 2 + 2 * y_item ** 2 + 1))
    min_fitnes = min(fit)
    min_fitnes_x = x[fit.index(min_fitnes)]
    min_fitnes_y = y[fit.index(min_fitnes)]
    max_fitnes = max(fit)
    max_fitnes_x = x[fit.index(max_fitnes)]
    max_fitnes_y = y[fit.index(max_fitnes)]
    fitnes_sorted = sorted(fit, reverse=True)
    for item in fitnes_sorted:
        x_new.append(round(x[fit.index(item)], 2))
        y_new.append(round(y[fit.index(item)], 2))
    return fit, fitnes_sorted,x_new, y_new, round(max_fitnes, 2), round(max_fitnes_x, 2), round(max_fitnes_y, 2), min_fitnes_x, min_fitnes_y




EPOCH_FITNESS, EPOCH_X_GEN, EPOCH_X_GEN=[], [], []

x1, y1 = population(x, y, POPULATION_SIZE)
for i in range(EPOCH):
    fitnes_list, fitnes_sorted, x_new, y_new, max_fitnes, max_fitnes_x, max_fitnes_y, min_fitnes_x, min_fitnes_y = fitnes(x1, y1)
    EPOCH_FITNESS.append(max_fitnes)
    EPOCH_X_GEN.append(min_fitnes_x)
    EPOCH_X_GEN.append(min_fitnes_y)
    x_new, y_new = new_population(x_new, y_new, x, y)
    x1 = x_new
    y1 = y_new


print(f"Fitnes: {EPOCH_FITNESS[-1]}, ({EPOCH_X_GEN[-1]}, {EPOCH_X_GEN[-1]})")
# draw_graph_input(x, y) #Berilgan Funksiya grafigi
draw_graph(EPOCH_FITNESS) #Epochlar bo'yicha grafik
