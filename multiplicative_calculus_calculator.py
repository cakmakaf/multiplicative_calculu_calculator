#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:52:57 2020

@author: ahmetcakmak
"""

import numpy as np 
class multplctv_clcltr:
    
    def m_addition(x,y):
        m_added = x * y
        print(m_added)
        
    def m_subtraction(x,y):
        m_sub = x / y
        print(m_sub)

    def m_multiplication(x,y):
        m_mult = x **(np.log(y))
        print(m_mult)

    def m_division(x,y):
        m_div = x **(1/np.log(y))
        print(m_div)
        




multplctv_clcltr.m_addition(2,8)
multplctv_clcltr.m_subtraction(2,8)           
multplctv_clcltr.m_multiplication(2,8)
multplctv_clcltr.m_division(2,8)