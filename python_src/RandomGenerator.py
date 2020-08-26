from numpy import random

def RandomGenerator(x, y):
    return random.uniform(x, y)

def gaussianRandomgenerator(x, y, mu, sigma):
    sample = random.normal(mu, sigma, None)
    if sample > y:
        sample = y
    elif sample < x:
        sample = x
    else:
        pass
    return sample
