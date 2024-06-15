# -------------------------------------------------------------------
# 15/06/2024
# Miscellaneous general purpose functions for algorithms
# Разные функции общего назначения для алгоритмов
#
# (C) 2024- Ivan Genik, Perm, Russia
# Released under GNU Public License (GPL)
# email igenik@rambler.ru
# -------------------------------------------------------------------

from math import isqrt

def list_of_primes_less_n(n):
    """
    based on 204 Count Primes https://leetcode.com/problems/count-primes/
    Given an integer n, return the prime numbers that are strictly less than n
    https://en.wikipedia.org/wiki/Prime_number
    https://en.wikipedia.org/wiki/List_of_prime_numbers

    Просто́е число́ — натуральное число, имеющее ровно два различных натуральных делителя.
    Другими словами, натуральное число p является простым, если оно отлично от 1
    делится без остатка только на и на само p
    """
    if n <= 1: return 0
    isq=isqrt(n)
    a=[True]*n
    for i in range(2,isq+1):
        if a[i]==True:
            j=0; nn=i**2
            while j<n:
                if nn <n:
                    a[nn]=False
                    j=j+1
                    nn=nn+i
                else: break
    return [i for i in range(2,n) if a[i]]

def test_primes():
    print(list_of_primes_less_n(11))

# the tests
if __name__ == "__main__":
    test_primes()