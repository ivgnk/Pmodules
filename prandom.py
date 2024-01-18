'''
Adding a random component to a given dataset
'''
import numpy as np
import matplotlib.pyplot as plt
import math

def linear_dat(n:int,a,b:float)->(np.ndarray,np.ndarray):
    x = np.linspace(0,n-1,n)
    y = a+b*x
    return x,y

def calc_descr_stat(x:np.ndarray):
    print(f'{np.min(x)=}')
    print(f'{np.max(x)=}')


# rnd_type
# 1 - rng.random
# 2 - uniform
# 3 - normal / gauss
# 4 - lognormal
nrnd_type = 3
a_=0; b_=0 # коэффициенты прямой y = a+b*x

def the_test_normal_graph():
    n = 100
    rng = np.random.default_rng(12345) #
    x,y = linear_dat(n,a_, b_)
    inid = 0.04
    lst = [inid, inid*10, inid*100, inid*1000]
    fig = plt.figure(figsize=(12,9))
    plt.suptitle('normal / gauss')
    for i,dat in enumerate(lst):
        print(i)
        plt.subplot(2,2,i+1)
        col = ('r','#1f77b4')[i==1]
        the_rnd_ = rng.normal(size=n, loc=0, scale=dat)
        s0 = f'Sgm = {dat}'
        s1 = f'Число N < 0 = {len(the_rnd_[the_rnd_<0])}' #    print(s1)
        s2 = f'Число N > 0 = {len(the_rnd_[the_rnd_>0])}' #    print(s2)
        # print(the_rnd_)
        plt.title(s0+'    '+s1+'    '+s2)
        plt.plot(x,the_rnd_, col)
        plt.grid()
    plt.show()

def the_test_normal_num():
    rng = np.random.default_rng(12345) #
    ddat = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    ddat2 = reversed(ddat)
    for i,x in enumerate(ddat2):
        dat = np.logspace(start=0.1, stop=10, base=1+x)
        # print(i,' ',len(dat))
        print(f'\n {i=} {x=} {(1+x)=}')
        print(dat)
        plt.scatter(dat,i*5+dat,label = str(1+x))
    plt.legend()
    plt.grid()
    plt.show()

def thetest1_random(a_:float, b_:float, rnd_type:int=1):
    n = 100
    rng = np.random.default_rng(12345)
    x,y = linear_dat(n,a_, b_)

    low_ = -1; high_ = 1
    # (b - a) * random() + a
    match rnd_type:
        case 1:
            the_rnd_ = rng.random(size=n);            name_rnd = 'random'
        case 2:
            the_rnd_ = rng.uniform(size=n);           name_rnd = 'uniform'
        case 3: # normal / gauss
        # normal(loc=0.0, scale=1.0, size=None)
        # loc : float or array_like of floats - Mean ("centre") of the distribution.
        # scale : float or array_like of floats -  Standard deviation (spread or "width") of the distribution. Must be non-negative.
            the_rnd_ = rng.normal(size=n, loc=0, scale=0.30);            name_rnd = 'normal / gauss'
            print(the_rnd_)
        case 4:
            the_rnd_ = rng.lognormal(size=n);         name_rnd = 'log normal'
        case other:
            the_rnd_ = rng.random(size=n);            name_rnd = 'random'
    the_rnd = low_ + the_rnd_ * (high_ - low_)
    calc_descr_stat(the_rnd)
#    y2 = x*the_rnd
    y3 = y*the_rnd
    y4 = y + y3
    plt.figure(figsize=(16, 9))
    plt.suptitle(name_rnd)
    plt.subplot(1, 2, 1)
    plt.plot(x,y,label='ini')
    plt.plot(x,the_rnd,label='rnd')
#    plt.plot(x,y2,label='x*rnd')
    plt.plot(x,y3, 'r--', label='y*rnd')
    plt.plot(x,y4, 'k--', label='y+y*rnd')
    plt.grid()
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x,y,label='ini')
    y5 = y + the_rnd
    plt.plot(x,y5, label='y+rnd')
    cf = 0.1
    y6 = y + y*the_rnd*cf
    plt.plot(x,y6, label='y+y*rnd*'+str(cf))
    plt.grid()
    plt.legend()

    plt.show()

if __name__ == "__main__":
    # thetest1_random(a_, b_, nrnd_type)
    # the_test_normal_graph() # Для разброса от -1 до 1 использовать Сигма (ст.откл) порядка 0.3
    the_test_normal_num()
