#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:09:08 2024

@author: meganfairchild
Find the sum of all the primes below two million.
"""
import math
primes = []
upperBound = 2000000

def is_it_prime(num):
    num=num
    #midpoint = math.floor((num+1)/2)
    #print("midpoint ", midpoint)
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:  # Eliminate even numbers early
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        #print("num is ", num)
        #print("midpoint is", midpoint)
        if num%i==0:
            #print("num mod i for i ", i, " is ", num%i)
            return False
        else:
            i+=1
    return True


j=2
for j in range(2, upperBound):
    boolfool = is_it_prime(j)
    if boolfool:
        primes.append(j)
        #print("the current list is: ", primes)
        j+=1
    else: 
       j+=1 

print("the sum of all primes is ", sum(primes))       
"""

Congratulations, the answer you gave to problem 10 is correct.

You are the 348131st person to have solved this problem.

You have earned 1 new award:

Decathlete: Solve ten consecutive problems"
"""    