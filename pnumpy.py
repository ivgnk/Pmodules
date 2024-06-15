# -------------------------------------------------------------------
# Разные функции для работы с Numpy
#
# (C) 2020-2024 Ivan Genik, Perm, Russia
# Released under GNU Public License (GPL)
# email igenik@rambler.ru
# -------------------------------------------------------------------
import inspect
import numpy as np

# https://habr.com/ru/articles/484136/
import math
from numba import njit
import pprint as pp
# import p1D_func_for_mininimizations as p1D
import matplotlib.pyplot as plt

lst_tst = [1.850721193459193e-05 + 0j,
        3.507267555276301e-05 - 4.257013639901627e-22j,
        3.803508129483612e-05 - 1.2443768064756367e-22j,
        3.829264588377769e-05 - 7.228876912647101e-22j,
        3.5515357472102105e-05 - 1.0676814419742923e-22j,
        3.3072437516413694e-05 + 2.0927650471641153e-22j,
        3.0475905508923024e-05 + 2.4289364243446022e-23j]


def tst_real_part():
    a = np.array(lst_tst,dtype=complex)
    print(a)
    b=real_part(a)
    print(b)

def tst_cmodule():
    a = np.array(lst_tst,dtype=complex)
    print(f'{abs(a)=}')
    print(f'{cmodule(a)=}')

def real_part(x:np.ndarray)->np.ndarray:
    ll=len(x)
    z =np.array([dat.real for dat in x])
    return z

def cmodule(x:np.ndarray)->np.ndarray:
    ll=len(x)
    z =np.array([abs(dat) for dat in x])
    return z


def tst_splitting_array():
    print('\nFunction', inspect.currentframe().f_code.co_name)
    nnpnt=1400   # points
    x=np.arange(nnpnt)
    ini=np.random.rand(nnpnt)
    n=10         # parts
    sx=splitting_array(x,n)
    si=splitting_array(ini,n)
    fig = plt.figure(figsize=(18,12))
    n_in_row=5
    for i in range(n):
        plt.subplot(2,n_in_row,i+1)
        plt.plot(sx[i],si[i])
        plt.grid()
    plt.show()

def splitting_array(ini:np.ndarray, n:int)->list:
    # part_1, part_2, part_3= values[0:parts], values[parts:(parts * 2)], values[(parts * 2):(parts * 3)]
    parts = int(len(ini) / n)
    res=[ini[(parts * i):(parts * (i+1))] for i in range(n)]
    return res



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

def thetest_find_min_max_in_2Dmatr_with_nan(f):
    x0 = np.linspace(-2,2,801)
    x1 = np.linspace(-4,4,801)
    x, y, z = f(x0,x1)
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

def thetest_logspace():
    arr = np.logspace(1, 4, num=12, base = 5)
    # array([  5.        ,   7.75529259,  12.02891263,  18.65754739,
    #         28.93894779,  44.88600147,  69.6208149 , 107.98595796,
    #        167.49253989, 259.79073064, 402.95062557, 625.        ])
    pp.pp(arr)


if __name__ == "__main__":
    # thetest_find_min_max_in_2Dmatr_with_nan()
    # thetest_logspace()
    # tst_splitting_array()
    # tst_real_part()
    tst_cmodule()
# test_findmax_arrindex1d()
# test_add_dat_in_list()

# https://riptutorial.com/ru/python/example/3973/бесконечность-и-nan---не-число--
# print( 100 > math.nan )