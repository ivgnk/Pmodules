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
nrnd_type = 4

def thetest1_random(rnd_type:int=1):
    n = 100
    rng = np.random.default_rng(12345)
    x,y = linear_dat(n,0.0,0.5)

    low_ = -1; high_ = 1
    # (b - a) * random() + a
    match rnd_type:
        case 1:
            the_rnd_ = rng.random(size=n);            name_rnd = 'random'
        case 2:
            the_rnd_ = rng.uniform(size=n);           name_rnd = 'uniform'
        case 3:
            the_rnd_ = rng.normal(size=n);            name_rnd = 'normal / gauss'
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
    thetest1_random(nrnd_type)
