'''
Functions for working with binary and hex data
'''
from s_math import _divmod


def int_to_bin(n: int) -> str:
    x = n
    b_str = ''
    while x > 0:
        q, r = _divmod(x, 2)
        x = q
        b_str = f'{r}{b_str}'
    return f'0b{b_str}'


def bin_to_int(n: str) -> int:
    v = 0
    i = 0
    for _ in range(len(n)):
        _i = int(n[::-1][i])
        v += ((2**i)*_i)
        i += 1
    return v
