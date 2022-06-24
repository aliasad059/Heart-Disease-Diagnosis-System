import numpy as np
from fuzzification import output_fuzzification


def center_of_gravity(x, y):
    """
        Calculate the center of gravity of a fuzzy set.
    """
    numerator = 0.
    denominator = 0.
    for i in enumerate(x):
        numerator += y[i[0]] * x[i[0]]
        denominator += y[i[0]]

    if denominator == 0:
        return 0.
    return numerator / denominator


def defuzzify(results):
    """
        Defuzzify the results of the fuzzy system.
    """
    outputs_membership = list(results.values())
    x = np.arange(0, 5, 0.001)
    y = np.zeros(len(x))
    for i0, i1 in enumerate(x):
        y[i0] = max(np.minimum(outputs_membership, output_fuzzification(i1)))
    return center_of_gravity(x, y)
