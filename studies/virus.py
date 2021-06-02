import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


GREY = (0.78, 0.78, 0.78)   #UNINFECTED
RED = (0.96, 0.15, 0.15)    #INFECTED
GREEN = (0, 0.86, 0.03)     #RECOVERED
BLACK = (0,0,0)             #DEAD

COVID19_PARAMS = {
    "r0": 2.28,
    "incubation": 5,
    "percent_mild": 0.8,
    "mild_recovery" : (7,14),
    "percent_severe": 0.2,
    "severe_recovery": (21,42),
    "severe_death": (14,56),
    "fatality_rate": 0.034,
    "serial_interval": 7
}

class Virus():
    def __init__(self, params):
        pass
    