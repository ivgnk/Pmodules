"""
Функции для работы с Pandas // Functions for work with Pandas
(C) 2024 Ivan Genik, Perm, Russia
Released under GNU Public License (GPL)
email igenik@rambler.ru
"""

from icecream import ic
import pandas as pd
from pstring import *


def create_dframe_from_leeetcode(fname:str, is_view:bool=True) -> pd.DataFrame:
    # https://habr.com/ru/companies/ruvds/articles/494720/
    with open(fname,"r") as f:
        lst = f.readlines()
    ll=len(lst)
    for i in range(ll):
        lst[i]=lst[i].replace('-','').replace('+','').replace('|','').replace('\n','')
    lst=remove_empty_strings(lst);ll=len(lst)
    col_names=lst[0].split()
    lst2=lst[1:]; lst2= [s.split() for s in lst2]
    df = pd.DataFrame(lst2)
    # https://vc.ru/u/1389654-machine-learning/752890-7-osnovnyh-sposobov-dlya-upravleniya-stolbcami-v-pandas
    df = df.rename(columns=dict(zip([i for i in range(ll)] ,col_names)))
    print(df)
    return df

if __name__ == "__main__":
    create_dframe_from_leeetcode('lc_1393.txt')



