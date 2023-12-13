# -------------------------------------------------------------------
# Модуль pstring, функции для работы со строками
# The string module, functions for working with strings
#
# (C) 2020-2023 Ivan Genik, Perm, Russia
# Released under GNU Public License (GPL)
# email igenik@rambler.ru
# ------------------------------
import re

def print_string(the_list) -> None:
    print(len(the_list))
    for stri in the_list:
        print(stri, end=' ')
    print('+')

def num_words_in_string(s: str) -> int:
    return len(re.split('\s+', s))

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

# thetest_is_number_()
thetest_num_words_in_string()



# Проработать строки и регулярные выражения
# pythonist.ru/s/proverka-yavlyaetsya-li-stroka-palindromom/?utm_source=turbo_turbo
# https://habr.com/ru/post/349860/

