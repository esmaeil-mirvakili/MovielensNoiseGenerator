import numpy as np
from scipy.stats import poisson


def poisson_noise(num, noise_level):
    if np.random.randint(100) <= noise_level:
        return poisson.rvs(num, size=1)[0]
    return num


def gaussian_noise(num, noise_level):
    if np.random.randint(100) <= noise_level:
        mu = 0
        sigma = 1
        return num + np.random.normal(mu, sigma, 1)[0]
    return num


def gender_flipping(sex, noise_level):
    if np.random.randint(100) <= noise_level:
        if sex == 'M':
            return 'F'
        return 'M'
    return sex
