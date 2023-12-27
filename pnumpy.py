# -------------------------------------------------------------------
# Разные функции для работы с Numpy
#
# (C) 2020 Ivan Genik, Perm, Russia
# Released under GNU Public License (GPL)
# email igenik@rambler.ru
# -------------------------------------------------------------------
import numpy as np

# https://habr.com/ru/articles/484136/
import math
from numba import njit
import p1D_func_for_mininimizations as p1D

@njit
def find_min_max_in_2Dmatr_with_nan(a)->(float, int, int, float, int, int):
    '''
    a - real matrix
    '''
    mmin =  1e32; imin = -1; jmin =-1
    mmax = -1e32; imax = -1; jmax =-1
    shp = a.shape
    # print(f'{shp=}')
    # print(f'{shp[0]=} {shp[1]=}')
    for i in range(shp[0]): # on raw
        for j in range(shp[1]):  # on col
            if not np.isnan(a[i,j]):
                if a[i,j]>mmax:
                    imax,jmax = i,j
                    mmax = a[i,j]
                if a[i,j]<mmin:
                    imin,jmin = i,j
                    mmin = a[i,j]
    return mmin, imin, jmin, mmax, imax, jmax

def thetest_find_min_max_in_2Dmatr_with_nan():
    x0 = np.linspace(-2,2,801)
    x1 = np.linspace(-4,4,801)
    x, y, z = p1D.for_eq016f(x0,x1)
    print(z)
    mmin, imin, jmin, mmax, imax, jmax = find_min_max_in_2Dmatr_with_nan(z)
    print(f'{mmin=}  {imin=}  {jmin=}')
    print(f'{mmax=}  {imax=}  {jmax=}')

def thetest_findmax_arrindex1d():
    x = np.array([112, 1111, 13, 14, 12, 11])
    llen = len(x)
    print(x)
    # !!! https://askdev.ru/q/kak-poluchit-indeksy-n-maksimalnyh-znacheniy-v-massive-numpy-4667/
    # print(np.argpartition(x, llen-1), end = '\n\n')
    z = (-x).argsort()[:llen]
    print(type(z))
    print(round(1.2), round(0.8))


def findmax_arrindex1d(x:np.ndarray):
    """
    Находит массив индексов элементов в порядке убывания
    x - одномерный массив
    :param num:
    :return:
    """
    llen:int = len(x)
    return (-x).argsort()[:llen]


def thetest_add_dat_in_ndarray():
    """
    Проверка создания "списка данных" на основе numpy
    """
    # numpy.vstack
    # https://pyprog.pro/array_manipulation/vstack.html
    arr = np.zeros(5)
    print(arr)
    for i in range(1,10):
        zz = np.zeros(5)
        zz = zz + i
        arr = np.vstack((arr, zz))
    print(arr)


def thetest_add_dat_in_ndarray2():
    """
    Проверка 2 создания "списка данных" на основе numpy
    https://coderoad.ru/568962/Как-создать-пустой-массив-матрицу-в-NumPy
    """
    arr = np.empty(shape= [0, 6])
    print(arr)
    for i in range(0,10):
        ll = [i*1, i*2, i*3, i*4, i*5, i*6]
        arr = np.append(arr, [ll], axis=0)
    print(arr)


def thetest_add_dat_in_list():
    """
    Проверка 2 создания списка данных
    """
    mylist = []
    for i in range(0,10):
        mylist.append([i*1, i*2, i*3, i*4, i*5, i*6 ])
    print(mylist)
    print(mylist[0])
    print(mylist[1])
    # mat = numpy.array(mylist)

if __name__ == "__main__":
    thetest_find_min_max_in_2Dmatr_with_nan()


# test_findmax_arrindex1d()
# test_add_dat_in_list()

# https://riptutorial.com/ru/python/example/3973/бесконечность-и-nan---не-число--
# print( 100 > math.nan )