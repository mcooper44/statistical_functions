'''
simple functions for probability distributions
'''
from s_math import _fact


def binom(n: int, r: int, p: float) -> float:
    '''
    Assumptions:
        observations are independent
        probability of success does not change
        from one trial to another

    n is the number of observations or trials
    r is the number of randomly selected items/outcomes
    p is the probability of success in each trial

    returns the probability of r in n trials as float
    '''
    nr = n - r # trial size - number of selected items
    c = _fact(n) / (_fact(r) * _fact((nr))) # combination of r from n
    pr = p ** r # probability to power of r successes
    f = (1 - p) # probability of failure
    return c * pr * (f ** nr)
