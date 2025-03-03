#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:17:16 2024

@author: meganfairchild

problem 2 from the project Euclid list 
problem: sum the even numbers in the fibonacci sequence whos values do not exceed four million
"""




fib1 = 1
fib2 = 1

sum = 0

while(fib2<4000000):
    if fib2 % 2 == 0:
        sum = sum + fib2
    temp = fib2
    fib2 = fib1 + fib2 
    fib1 = temp 
    
print(sum)    
        

"""
Congratulations, the answer you gave to problem 2 is correct.

You are the 809525th person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%
"""
