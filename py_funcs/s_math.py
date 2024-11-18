'''
Home brew math functions
'''
from collections.abc import Iterable
from typing import Union


def _divmod(a: int, b: int) -> tuple:
    return (a // b, a % b)


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

def pad_to_base(n: int, base: int = 4) -> int:
    '''
    Provides integer value needed to pad a string
    so that it is of a specified length.
    This function is needed to determine how many 0's 
    need to be pre-pended to a binary string so that
    it is a multiple of 4 bits long.
    '''
    padding = 0
    while (n + padding) % base !=0:
        padding += 1
    return padding

def pad_to_n(b: str, n: int) -> list:
    '''
    Prepends n 0's to a binary string
    '''
    return f'{'0'*n}{b}'
