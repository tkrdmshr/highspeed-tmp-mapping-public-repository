#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def lifetime_to_temperature_201112(x):
    temperature = 0.0603644272864967*(x**5) - 2.27554925190688*(x**4) + 34.1786499772982*(x**3) - 255.366668663145*(x**2) + 949.582685485572*x - 1381.94789212487
    return temperature



def pict_calibration(content, xmin, xmax, dim):
    temperature = pd.read_csv(content + '.csv').iloc[:, 1]
    lifetime = pd.read_csv(content + '.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, dim)
    p = np.poly1d(z)
    xp = np.linspace(xmin, xmax ,800)
    print(p)
    plt.plot(temperature, lifetime, '.', p(xp), xp, '-')
    plt.show()
