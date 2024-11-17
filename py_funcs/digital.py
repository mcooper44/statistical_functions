'''
Functions for working with binary and hex data
'''
from s_math import _divmod
from s_math import pad_to_base
from s_math import _sum

# Binary to Hex lookup
B2H_LU = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

# Hex to binary lookup
H2B_LU = {
         '0': '0000', '1': '0001', '2': '0010', '3': '0011',
         '4': '0100', '5': '0101', '6': '0110', '7': '0111',
         '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
         'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

HEX_VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
              '9', 'A', 'B', 'C', 'D', 'E', 'F']


def int_to_bin(n: int, flag: bool = False) -> str:
    x = n
    b_str = ''
    while x > 0:
        q, r = _divmod(x, 2)
        x = q
        b_str = f'{r}{b_str}'
    return f'0b{b_str}' if flag else b_str


def bin_to_int(n: str, flag: bool = False) -> int:
    v = 0
    i = 0
    if flag: n = n[2:]
    for _ in range(len(n)):
        _i = int(n[::-1][i])
        v += ((2**i)*_i)
        i += 1
    return v


def int_to_hex(n: int, flag: bool = False) -> str:
    bin_val = int_to_bin(n)
    pad = pad_to_base(len(bin_val), 4)
    bin_str = f'{'0'*pad}{bin_val}'
    bin_seg = [bin_str[i:i+4] for i in range(0, len(bin_str), 4)]
    hex_val = ''.join(B2H_LU.get(s, '') for s in bin_seg)
    return f'0x{hex_val}' if flag else hex_val


def bin_to_hex(b: str, flag: bool = False) -> str:
    if flag: b = b[2:]
    return int_to_hex(bin_to_int(b), flag)


def hex_to_bin(h: str, flag: bool = False) -> str:
    if flag: h = h[2:]
    return ''.join(H2B_LU.get(char, '') for char in h)


def hex_to_int(h: str, flag: bool = False) -> int:
    if flag: h = h[2:]
    multiplier = [int(HEX_VALUES.index(v)) for v in h[::-1]]
    return _sum(m*(16**p) for m,p in zip(multiplier, range(0, len(h))))


