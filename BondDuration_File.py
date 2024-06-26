#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:08:27 2024

@author: suzy
"""

import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    couponPayment = face * couponRate / ppy
    periods = np.arange(1, m * ppy + 1)
    discountFactors = (1 + y / ppy) ** (-periods)
    couponPV = couponPayment * discountFactors
    facePV = face / (1 + y / ppy) ** (m * ppy)
    bondPrice = np.sum(couponPV) + facePV
    weightedTime = periods * couponPV
    totalWeightedTime = np.sum(weightedTime) + (m * ppy * facePV)
    duration = totalWeightedTime / bondPrice / ppy
    
    return duration


