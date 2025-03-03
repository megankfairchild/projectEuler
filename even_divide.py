#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:02:38 2024

@author: meganfairchild

find the smallest number that is evenly divisible by the numbers 1-20
"""

def divide_check(num):
    num=num
    i=2
    while i<21:
        if num%i!=0:
            #print("mod arithmatic gives ", num%i)
            return(1)
        else:
            i+=1
            #print("i is now", i)
            
    return(0)      

candidate = 20
x=1
while x==1:
    #print("candidate is ", candidate)
    x = divide_check(candidate)
    if x==0:
        print("smallest number is ", candidate) 
    #rint("value is ", value)
    candidate +=1 
    
    
print("done")    

"""
Congratulations, the answer you gave to problem 5 is correct.

You are the 518040th person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%.
"""