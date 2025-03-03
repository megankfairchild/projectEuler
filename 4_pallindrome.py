#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:51:20 2024

@author: meganfairchild

pallindrome numbers problem: Find the largest palindrome made from the product of two 3-digit numbers.
"""

#import numpy as np

pall = []

def is_it_pal(num):
    x = num
    # Convert the number to a string, iterate through each character, and convert it back to an integer
    digits = [int(digit) for digit in str(x)]
    #need the length to see if it is even or odd. 
    l = len(digits)-1
    dummy = l
    
    if l%2==1:
        k=0
        while dummy >= (l+1)/2:
            if digits[k] != digits[dummy]:
                return(1)
            else:
                if k==(l-1)/2:
                    return(0)
                else:
                    k+=1
                    dummy = dummy-1
                    
    if l%2==0:
        k=0
        while dummy >= (l+1)/2:
            if digits[k] != digits[dummy]:
                return(1)
            else:
                k+=1 
                dummy = dummy-1
            
    return(0)
       
                    
i = 100

while(i<1000): 
    j = 100
    while(j<1000):
        prod = i*j
        y = is_it_pal(prod) 
        if y==0:
            pall.append(prod)
            j+=1
        else:
            j+=1
    i+=1 
            
   
l = len(pall)
max=pall[0]

while(i<l):
    if pall[i]>max:
        max = pall[i]
        i+=1
    else:
        i+=1
        
        
print("the largest pall is ", max)
    
"""
Congratulations, the answer you gave to problem 4 is correct.

You are the 515473rd person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 
"""
