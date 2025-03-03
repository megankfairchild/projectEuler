#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:33:22 2024

@author: meganfairchild

problem 3: What is the largest prime factor of the number 600851475143?
"""

factors = []
num = 600851475143

upperbound = num/2
i = 2
print(upperbound)

while(i < upperbound and num!=1):
    if num % i == 0:
        factors.append(i)
        num = int(num/i)
    else:
        i += 1

large = factors[0]   
length = len(factors) 
i=1

while(i<length):
    if factors[i]>factors[0]:
        large = factors[i]
        i+=1
    else: 
        i+=1

print(large)
print(factors)
    
"""
    Congratulations, the answer you gave to problem 3 is correct.

You are the 583119th person to have solved this problem.

You have earned 1 new award:

Baby Steps: Solve three problems


This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.
"""
