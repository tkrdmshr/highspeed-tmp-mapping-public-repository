#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def intensity_ratio_to_temperature(value):
    temperature = pd.read_csv('intensity_increase_ratio.csv')['temperature']
    increase_ratio = pd.read_csv('intensity_increase_ratio.csv')['intensity_ratio']
    z = np.polyfit(increase_ratio, temperature, 3)
    p = np.poly1d(z)
    return p(value)



def temperature_to_intensity_ratio(value):
    temperature = pd.read_csv('intensity_increase_ratio.csv')['temperature']
    increase_ratio = pd.read_csv('intensity_increase_ratio.csv')['intensity_ratio']
    z = np.polyfit(temperature, increase_ratio, 3)
    p = np.poly1d(z)
    return p(value)



def temperature_to_lifetime(value):
    temperature = pd.read_csv('lifetime.csv').iloc[:, 1]
    increase_ratio = pd.read_csv('lifetime.csv').iloc[:, 2]
    z = np.polyfit(temperature, increase_ratio, 5)
    p = np.poly1d(z)
    return p(value)

def temperature_to_lifetime_201112(x):
    lifetime = -0.0000306193804481857*(x**5) + 0.00504273449558168*(x**4) - 0.328588984620315*(x**3) + 10.5612583357351*(x**2) - 166.721803292097*x + 1036.71905950018
    return lifetime


def temperature_to_lifetime_int_weight(value):
    temperature = pd.read_csv('lifetime_int_weight.csv').iloc[:, 1]
    increase_ratio = pd.read_csv('lifetime_int_weight.csv').iloc[:, 2]
    z = np.polyfit(temperature, increase_ratio, 3)
    p = np.poly1d(z)
    return p(value)




def lifetime_to_temperature(value):
    temperature = pd.read_csv('lifetime.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)


def lifetime_to_temperature_201112(x):
    temperature = 0.0603644272864967*(x**5) - 2.27554925190688*(x**4) + 34.1786499772982*(x**3) - 255.366668663145*(x**2) + 949.582685485572*x - 1381.94789212487
    return temperature

def lifetime_to_temperature_int_weight_201112(x):
    temperature = 0.21610909647624*(x**5) - 8.89216113498564*(x**4) + 145.977687*(x**3) - 1194.711705*(x**2) + 4875.1463096801*x - 7912.91576491343
    return temperature

def lifetime_to_temperature_recealed(value):
    temperature = pd.read_csv('lifetime_recealed.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_recealed.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 5)
    p = np.poly1d(z)
    return p(value)


def lifetime_to_temperature_int_weight(value):
    temperature = pd.read_csv('lifetime_int_weight.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_int_weight.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)


def lifetime_to_temperature_GEL(value):
    temperature = pd.read_csv('lifetime_gel.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_gel.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_cyto(value):
    temperature = pd.read_csv('lifetime_cyto.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_cyto.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_nuc(value):
    temperature = pd.read_csv('lifetime_nuc.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_nuc.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 5)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_DMEM(value):
    temperature = pd.read_csv('lifetime_DMEM.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_DMEM.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_before(value):
    temperature = pd.read_csv('lifetime_before.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_before.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_lin32(value):
    temperature = pd.read_csv('lifetime_lin32.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_lin32.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 1)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_lin42(value):
    temperature = pd.read_csv('lifetime_lin42.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_lin42.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_lin42_CHO(value):
    temperature = pd.read_csv('lifetime_lin42_CHO.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_lin42_CHO.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_PEG10k(value):
    temperature = pd.read_csv('lifetime_PEG10k.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_PEG10k.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)


def lifetime_to_temperature_PEO(value):
    temperature = pd.read_csv('lifetime_PEO.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_PEO.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)


def lifetime_to_temperature_water(value):
    temperature = pd.read_csv('lifetime_water.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_water.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_water_gel13(value):
    temperature = pd.read_csv('lifetime_gel_water.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_gel_water.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 5)
    p = np.poly1d(z)
    return p(value)

def lifetime_to_temperature_PEG1000(value):
    temperature = pd.read_csv('lifetime_PEG1000.csv').iloc[:, 1]
    lifetime = pd.read_csv('lifetime_PEG1000.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def intensity_to_temperature_GEL(value):
    temperature = pd.read_csv('calibration_GEL.csv').iloc[:, 1]
    intensity = pd.read_csv('calibration_GEL.csv').iloc[:, 2]
    z = np.polyfit(intensity, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def temperature_to_intensity_GEL(value):
    temperature = pd.read_csv('calibration_GEL.csv').iloc[:, 1]
    intensity = pd.read_csv('calibration_GEL.csv').iloc[:, 2]
    z = np.polyfit(temperature, intensity, 4)
    p = np.poly1d(z)
    return p(value)

def Long_lifetime_ratio_to_temperature(value):
    temperature = pd.read_csv('Long_lifetime_ratio.csv').iloc[:, 1]
    lifetime = pd.read_csv('Long_lifetime_ratio.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 3)
    p = np.poly1d(z)
    return p(value)

def pict_calibration(content, xmin, xmax, dim):
    temperature = pd.read_csv(content + '.csv').iloc[:, 1]
    lifetime = pd.read_csv(content + '.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, dim)
    p = np.poly1d(z)
    xp = np.linspace(xmin, xmax ,800)
    print(p)
    plt.plot(temperature, lifetime, '.', p(xp), xp, '-')
    plt.show()

def pict_calibration_GEL(content):
    temperature = pd.read_csv(content + '.csv').iloc[:, 1]
    lifetime = pd.read_csv(content + '.csv').iloc[:, 2]
    z = np.polyfit(lifetime, temperature, 4)
    p = np.poly1d(z)
    xp = np.linspace(0, 1.2 ,800)
    plt.plot(lifetime, temperature, '.', xp, p(xp), '-')
    plt.show()


def Rhodamine_B(value):
    temperature = pd.read_csv('lifetime_RhodamineB.csv')['temperature']
    lifetime = pd.read_csv('lifetime_RhodamineB.csv')['lifetime']
    z = np.polyfit(lifetime, temperature, 1)
    p = np.poly1d(z)
    return p(value)


def RhodamineB_water(value):
    temperature = pd.read_csv('lifetime_RhodamineB_water.csv')['temperature']
    lifetime = pd.read_csv('lifetime_RhodamineB_water.csv')['lifetime']
    z = np.polyfit(lifetime, temperature, 1)
    p = np.poly1d(z)
    return p(value)


def heatmap(value, range):
    plt.figure()
    plt.rcParams["font.size"] = 18
    sns.heatmap(value, square = True, cmap = "jet", vmin=range[0], vmax=range[1], xticklabels = False, yticklabels = False)
    plt.show()
