# -------------------------------------------------------------------
# Модуль pstring, функции для работы со строками
# The string module, functions for working with strings
#
# (C) 2020-2023 Ivan Genik, Perm, Russia
# Released under GNU Public License (GPL)
# email igenik@rambler.ru
# ------------------------------


vowel_low=['a', 'e', 'i', 'o', 'u']
vowel_hgh=['A', 'E', 'I', 'O', 'U']
a_all='abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a_low='abcdefghijklmnopqrstuvwxyz'
a_hgh='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a_num = '0123456789'
a_low_rev='zyxwvutsrqponmlkjihgfedcba'
a_low_circle='zyxwvutsrqponmlkjihgfedcbabcdefghijklmnopqrstuvwxyz'

a_hgh_l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']

lh_p=['aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH', 'iI', 'jJ', 'kK', 'lL', 'mM', 'nN', 'oO', 'pP', 'qQ', 'rR', 'sS', 'tT', 'uU', 'vV', 'wW', 'xX', 'yY', 'zZ']
hl_p=['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']

import re
import inspect

def make_pairs():
    ll=len(a_low)
    s1 = [a_low[i]+a_hgh[i] for i in range(ll)]
    print(s1)
    s2 = [a_hgh[i]+a_low[i] for i in range(ll)]
    print(s2)
    print(ord('A')-ord('a'), ord('a')-ord('A'))

def print_string(the_list) -> None:
    print(len(the_list))
    for stri in the_list:
        print(stri, end=' ')
    print('+')

def remove_letters(s:str)->str:
    return ''.join([ss for ss in s if ss in '0123456789'])

def num_words_in_string(s: str) -> int:
    return len(re.split(r'\s+',s)) # ???

def swlz(num:int, nposit:int) -> str: # строка с ведущими нулями
    """
    https://ru.stackoverflow.com/questions/628701/Вывод-числа-с-ведущими-нолями
    Вывод числа с ведущими нолями
    :param num:  число для преобразования в строку
    :param nposit: всего позиций в строке
    :return: строка с ведущими нулями
    """
    return str(num).zfill(nposit)

# определяет число ли это
def is_number_(thestring):
    # https://defpython.ru/proverit_yavlyaetsya_li_stroka_czislom_v_Python или https://all-python.ru/osnovy/proverka-na-chislo.html
    if thestring.isdigit():
        return True
    else:
        try:
            float(thestring)
            return True
        except ValueError:
            return False

# удаляет пустые строки из списка
def remove_empty_strings(ini_list):   # на входе список строк
    # http://espressocode.top/python-remove-empty-strings-from-list-of-strings - Способ № 4: Использование filter()
    x2 = list(filter(None, ini_list))
    return x2

#------------------------------------------------------------------------
#-------- Тестирование функций
def thetest_is_number_():
    print(''.isdigit())
    print('dd'.isdigit())
    print(is_number_('1'))
    print(is_number_('12'))
    print(is_number_('12a'))
    print(is_number_('a12'))
    print(is_number_('12e32'))
    print(is_number_('12e-32'))
    print(is_number_('12.0'))
    print(is_number_('12.0e43'))
    print(is_number_('12.0e-43'))
    print(is_number_('12.0.'))
    print(is_number_('12.0.1'))
    print(is_number_('.12.0.1'))

def thetest_empty_strings():
    #ini_list=["","1111","","","2222",""," "]
    s='111.4 222.555   3E-4   '
    ini_list=s.split()
    print(ini_list)
    ini_list=remove_empty_strings(ini_list)
    print(ini_list)

def thetest_num_words_in_string():
    print(re.sub(r'\D', '', 'Fjkoweuqe -1245 654lfr'))
    print(num_words_in_string('In the hole in the ground there lived a   hobbit')) # 10
    print(num_words_in_string('В  яме в  земле   жил   хоббит')) # 6
    print(num_words_in_string('min1')) # 1

def thetest_remove_letters():
    print('\nFunction', inspect.currentframe().f_code.co_name)
    print(remove_letters('min1'))
    print(remove_letters('win 13'))
    print(remove_letters('2 win 13'))

def the_test_new_split():
    s= 'sss ddd ffgg.  .  gggg ggg'
    s =' 7.5  6666 66.8888   ddd  dd ----   ' # 6
    # https://docs.python.org/3/library/re.html
    print(f'{s=}')
    print()
    print(r'\S+  ', re.split(r'\S+',s))
    print(r'\s+',re.split(r'\s+',s))
    print()
    print(r'\W+  ', re.split(r'\W+',s))
    print(r'(\W+)',re.split(r'(\W+)',s))
    print(r'\w+  ',re.split(r'\w+',s))

    print(f'{num_words_in_string(s)=}')

# thetest_is_number_()
if __name__ == "__main__":
    # thetest_num_words_in_string()
    # thetest_remove_letters()
    # the_test_new_split()
    # make_pairs()
    print(a_low[::-1])

# Проработать строки и регулярные выражения
# pythonist.ru/s/proverka-yavlyaetsya-li-stroka-palindromom/?utm_source=turbo_turbo
# https://habr.com/ru/post/349860/

