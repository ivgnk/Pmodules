'''
some trigonometric functions and explanations for them
'''
import numpy as np
import matplotlib.pyplot as plt


def horiz_line_sin_cos():
    maxn = 100
    num = 101
    fig = plt.figure(figsize=(12,9))
    x = np.linspace(0,maxn, num)
    nper = 2
    plt.suptitle('Синусы и косинусы')

    plt.subplot(2,2,1)
    plt.title('Половина периода')
    x2 = x*np.pi/num; ysin = np.sin(x2); ycos = np.cos(x2)
    plt.plot(x,ysin,label='sin'); plt.plot(x,ycos,label='cos'); plt.legend()
    plt.grid()

    plt.subplot(2,2,2)
    plt.title('Период (*2)')
    x2 = x*np.pi/num*2; ysin = np.sin(x2); ycos = np.cos(x2)
    plt.plot(x,ysin,label='sin'); plt.plot(x,ycos,label='cos'); plt.legend()
    plt.grid()

    plt.subplot(2,2,3)
    plt.title('2 Периода (*4)')
    x2 = x*np.pi/num*4; ysin = np.sin(x2); ycos = np.cos(x2)
    plt.plot(x,ysin,label='sin'); plt.plot(x,ycos,label='cos'); plt.legend()
    plt.grid()

    plt.subplot(2,2,4)
    plt.title('3 Периода (*6)')
    x2 = x*np.pi/num*6; ysin = np.sin(x2); ycos = np.cos(x2)
    plt.plot(x,ysin,label='sin'); plt.plot(x,ycos,label='cos'); plt.legend()
    plt.grid()

    plt.show()

def nperiod_fun(f:np.ufunc,x:np.ndarray, nper:float, is_view=False)->(np.ndarray):
    num = len(x)
    x2 = x * np.pi / num * nper*2
    y =f(x2)
    if is_view:
        plt.title(f' {f.__name__} {nper} период(ов)')
        plt.plot(x, y)
        plt.grid()
        plt.show()
    return y

def thetest_nperiod_sin_cos(thefunc:str):
    maxn = 199
    num = 200
    x = np.linspace(0,maxn, num)
    fig = plt.figure(figsize=(12,9))
    if thefunc.lower() == 'sin':
        titname = 'Синусы'; f = np.sin
    else:
        titname = 'Косинусы'; f = np.cos
    plt.suptitle(titname)
    for i in [1,2,3,4]:
        y = nperiod_fun(f,x,i)
        plt.subplot(2,2,i)
        plt.title(f'{i} Период(а)')
        plt.plot(x, y)
        plt.grid()
    plt.show()

    nperiod_fun(f, x, 3, is_view = True)
    plt.show()

def horiz_line_sin_cos2():
    pass


if __name__ == "__main__":
    thetest_nperiod_sin_cos('sin')
    # thetest_nperiod_sin_cos('cos')
