#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:20:20 2024

@author: meganfairchild

find the 10,001th prime number
"""

primes =[2]
ultimate = 10001
i=0

def is_it_prime(num):
    num=num
    j=2
    while(j<num):
        if num%j == 0:
            return 1
        else:
            if j==num-1:
                return 0
            else:
                j+=1
                
while(len(primes)<ultimate):
    x = is_it_prime(i)
    if x==0:
        primes.append(i) 
    i+=1
    
print("The list of primes is ", primes)

print("The ", ultimate, " prime is ", primes[ultimate-1])    
        
""" 
Congratulations, the answer you gave to problem 7 is correct.

You are the 446181st person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%
"""