'''
functions to measure central tendancy

'''
from collections.abc import Iterable
from typing import Union


def _product(itrble: Iterable) -> Union[int, float]:
    n = 1
    for i in itrble:
        n *= i
    return n


def _sum(itrble: Iterable) -> Union[int, float]:
    n = 0
    for i in itrble:
        n += i
    return n


def _sqrt(S: Union[int, float], precision: int = 11) -> float:
    '''

    This is a simple implementation of the Babylonian method
    to find the sqrt of S pick a number x_0 that you think
    might be correct. And apply x_1 = (x_0 + S / x_0)/2
    and iterate until x_n+1 and x_n agree to as many decimal
    points as you desire
    '''
    if int(S) == 0:
        return 0.0
    if S < 0:
        raise ValueError('negative input not in domain of possible squares')
    x = S/2  # start with a guess
    x_n = 0
    for _ in range(precision):
        x = (x + (S/x))/2
        if x_n == x:  # we have convergence
            return x
        x_n = x
    return x_n  # iterated precision times w/o convergence


def geometric_mean(x_array: Iterable) -> float:
    '''
    Used to find the average of %, ratios, indexes or
    growth rates
    '''
    return _product(x_array)**(1.0/len(x_array))


def sample_mean(x_array: Iterable) -> float:
    return _sum(x_array)/len(x_array)


def population_mean(x_array: Iterable) -> float:
    return sample_mean(x_array)


def weighted_mean(x_array: Iterable) -> float:
    '''
    multiplies each observation by the number of times
    it happens divided by the sum of occurances
    Useful for situations such as find the mean of
    S,M,L product sales
    '''
    v_w = {x: x_array.count(x) for x in set(x_array)}
    return _sum([x*y for x, y in v_w.items()])/_sum(v_w.values())


def statistical_range(x_array: Iterable) -> Union[int, float]:
    '''
    The range between the largest and smallest value in
    the sample of values
    '''
    return max(x_array) - min(x_array)


def mean_absolute_deviation(x_array: Iterable) -> float:
    '''
    The sum of the absolute of each  value in the sample minus the mean
    of the sample.
    '''
    m = sample_mean(x_array)
    return _sum([abs(x-m) for x in x_array]) / len(x_array)


def variance(x_array: Iterable) -> float:
    '''
    The arithmetic mean of the squared deviations of the mean.
    This yields the sample variance.
    '''
    m = sample_mean(x_array)
    return _sum([(x-m)**2 for x in x_array])/(len(x_array)-1)


def standard_deviation(x_array: Iterable) -> float:
    '''
    returns the sample standard deviation of an array
    '''
    return _sqrt(variance(x_array))


def standard_error_mean(x_array: Iterable) -> float:
    '''
    returns the sample standard error of the mean
    '''
    return standard_deviation(x_array) / _sqrt(len(x_array))
