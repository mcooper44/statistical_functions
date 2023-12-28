'''
Functions for working with binary and hex data
'''
from typing import Union
from s_math import _divmod


def int_to_bin(n: Union[int, float]) -> str:
    x = n
    b_str = ''
    while x > 0:
        q, r = _divmod(x, 2)
        x = q
        b_str = f'{r}{b_str}'
    return f'0b{b_str}'
