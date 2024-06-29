# -------------------------------------------------------------------
# 15/06/2024
# Miscellaneous general purpose functions
# Разные функции общего назначения
#
# (C) 2020-2024 Ivan Genik, Perm, Russia
# Released under GNU Public License (GPL)
# email igenik@rambler.ru
# -------------------------------------------------------------------

import math
import numpy as np

# https://barzunov.ru/2022/12/numbering-system-conversion-in-python/
def convert_to2(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

# https://ru.stackoverflow.com/questions/1297746/Перевод-систем-счисления
def convert_to(n, base):
    string = ''
    while n > 0:
        string += str(n % base)
        n //= base
    return string[::-1]

def shift_list2(lst, k):
    # https://leetcode.com/problems/rotate-list/solutions/5227088/simple-python-solution-using-list-beats-95-running-time/
    ll = len(lst)
    if k >= ll:
        k -= (k // ll) * ll
    # Rotate the list
    return  lst[ll - k:] + lst[:ll - k]

# https://bobbyhadz.com/blog/how-to-shift-rotate-list-in-python
def shift_list(lst, index=1):
    index = index % len(lst)
    return lst[index:] + lst[:index]


def out_of_diap2(dat, dat_min, dat_max) -> (float, float):
    """
    Расчет выхода за диапазон - абсолютные и относительные значения (доли 1)
    """
    llen = dat_max-dat_min
    if (dat_min > dat):
        d = dat_min - dat
        return d, d/llen
    if (dat_max < dat):
        d = dat - dat_max
        return d, d/llen

def out_of_diap1proc(dat, dat_min, dat_max) -> float:
    """
    Расчет выхода за диапазон - относительные значения (доли 1)
    """
    llen = dat_max-dat_min
    if (dat_min > dat):
        d = dat_min - dat
        return d/llen
    if (dat_max < dat):
        d = dat - dat_max
        return d/llen

def out_of_diap2proc(dat, dat_min, dat_max) -> float:
    """
    Расчет выхода за диапазон - абсолютные и относительные значения (доли 1)
    Вычисления в логарифмическом масштабе
    """
    dat_minln = math.log10(dat_min); # print(dat_min)
    dat_maxln = math.log10(dat_max)
    if dat<0:
        dat_ln = -10
    else:
        dat_ln = math.log10(dat)

    llen = dat_maxln-dat_minln
    d = 0
    if (dat_minln > dat_ln):
        d = dat_minln - dat_ln
    if (dat_maxln < dat_ln):
        d = dat_ln - dat_max
    # print(d/llen)
    return abs(d/llen)



def dat_in_diap(dat, dat_min, dat_max) -> bool:
    return ((dat_min <= dat) and (dat <= dat_max))

def dat2_in_diap(dat1, dat2, dat_min, dat_max, isview:bool=False) -> bool:
    if isview: print(dat1, dat2, dat_min, dat_max)
    return (dat_min <= dat1) and (dat1 <= dat_max) and (dat_min <= dat2) and (dat2 <= dat_max)

def create_2d_nparray_r1c2(row, col, dat00 = 0.0, dat01 = 0.0) -> object:
    a = np.zeros((row, col), dtype=object)
    a[0, 0] = dat00
    a[0, 1] = dat01
    return a

def add_2d_nparray(nparr1, dat00, dat01) -> object:
    # Функции numpy.hstack() и numpy.vstack()
    # https://pythonist.ru/funkczii-numpy-hstack-i-numpy-vstack/
    nparr2 = create_2d_nparray_r1c2(1, 2, dat00, dat01)
    return np.vstack((nparr1, nparr2))

def test_2d_nparray() -> None:
    nparr = create_2d_nparray_r1c2(1,2)
    print(nparr, end='\n\n')
    nparr = add_2d_nparray(nparr, 10, 20)
    print(nparr)

def print_format_examples():
    f = 2700.567
    print('f=', f)
    print('f = %7.3f' % f)

if __name__ == "__main__":
    print(convert_to(34, 6))

# print(dat2_in_diap(0.001, 9.999, 0.0, 10.0, isview=True))
# print(dat2_in_diap(float('nan'), float('nan'), float('nan'), float('nan'), isview=True))
# test_2d_nparray()
# print_format_examples()


