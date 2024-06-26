#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:59:10 2024

@author: suzy
"""

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    couponPayment = face * couponRate / ppy
    
    periods = np.arange(1, m * ppy + 1)

    couponPV = couponPayment / (1 + y / ppy) ** periods
    
    facePV = face / (1 + y / ppy) ** (m * ppy)
    
    bondPrice = np.sum(couponPV) + facePV
    return bondPrice


        