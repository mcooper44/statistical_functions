'''
Functions for working with binary and hex data
'''
from s_math import _divmod
from s_math import pad_to_base

def int_to_bin(n: int, flag: bool = False) -> str:
    x = n
    b_str = ''
    while x > 0:
        q, r = _divmod(x, 2)
        x = q
        b_str = f'{r}{b_str}'
    return f'0b{b_str}' if flag else b_str


def bin_to_int(n: str) -> int:
    v = 0
    i = 0
    for _ in range(len(n)):
        _i = int(n[::-1][i])
        v += ((2**i)*_i)
        i += 1
    return v


def int_to_hex(n: int, flag: bool = False) -> str:
    lu = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    bin_val = int_to_bin(n)
    pad = pad_to_base(len(bin_val), 4)
    bin_str = f'{'0'*pad}{bin_val}'
    bin_seg = [bin_str[i:i+4] for i in range(0, len(bin_str), 4)] 
    hex_val = ''.join(lu.get(s, '') for s in bin_seg)
    return f'0x{hex_val}' if flag else hex_val
