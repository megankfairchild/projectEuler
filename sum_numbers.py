#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:43:56 2024

@author: meganfairchild
"""

"""
Let's solve some project Euclid problems. 
""" 

#GOAL: calculate the sum of all multiples of 3 and 5 that are less than 1000. 

import pandas as pd 
sum = 0 

i = 1
while i<1000:
    if i % 3 == 0:
        sum = sum + i
        i += 1
    else: 
        i += 1

print(sum) 

i=1
while i<1000:
    if i % 5 == 0:
        if i % 3 == 0:
            i += 1
        else:
            sum = sum + i
            i += 1
    else: 
        i += 1
        
print(sum)         

"""
Congratulations, the answer you gave to problem 1 is correct.

You are the 1016027th person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you had previously solved was 0%. 
This is a new record. Well done!
"""