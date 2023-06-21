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


def _sqrt(x: Union[int, float], precision: int = 10) -> float:
    '''
    This is a simple implementation of the Babylonian method
    '''
    n = 1
    y = x
    for _ in range(precision):
        y = (y + n) / 2
        n = x / y
    return y


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
    The arithmetic mean of the squared deviations of the mean
    '''
    m = sample_mean(x_array)
    return _sum([(x-m)**2 for x in x_array])/len(x_array)


def standard_deviation(x_array: Iterable) -> float:
    return _sqrt(variance(x_array))
