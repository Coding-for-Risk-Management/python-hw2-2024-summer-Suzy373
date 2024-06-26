#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:13:38 2024

@author: suzy
"""

import numpy as np
def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1, dtype=object)
    
    result = numbers.astype(str)
    result[(numbers % 3 == 0) & (numbers % 5 == 0)] = 'fizzbuzz'
    result[(numbers % 3 == 0) & (numbers % 5 != 0)] = 'fizz'
    result[(numbers % 5 == 0) & (numbers % 3 != 0)] = 'buzz'
    
    return result
