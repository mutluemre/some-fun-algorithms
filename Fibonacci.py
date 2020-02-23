# -*- coding: utf-8 -*-
"""
author: Emre Mutlu
Date: Sat Feb 22 22:06:51 2020
"""

def fibonacci(n):
    liste=[1,1]
    while len(liste)<n:
        liste.append(liste[-1]+liste[-2])
    return liste[-1]

def fibrecursion(n):
    if n==1 or n==2:
        return 1
    else:
        return fibrecursion(n-1)+fibrecursion(n-2)

if __name__=="__main__":
    print fibonacci(10)
    print fibrecursion(10)