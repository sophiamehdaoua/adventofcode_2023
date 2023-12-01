# -*- coding: utf-8 -*-

"""
Task:
- inputs are a random string of letters and numbers e.g. fivepqxlpninevh2xxsnsgg63pbvdnqptmg
- objective is to get take the first and last numbers in that string e.g. 23
- this needs to be done for 1000 inputs 
- we then need to sum all of those values 

"""

import pandas as pd 
import numpy as np


day1csv= pd.read_csv(r"C:/Users/sophi/Downloads/adventofcode_day1_2023.csv")

# creating translation table to remove letters
remove_letters = str.maketrans(
    "", "", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

#1. create empty list, 2.removeletters 3.take the first and last values
listofnumbers=[]
for i in range(0, len(day1csv)):
    listofnumbers.append((day1csv.inputs[i].translate(remove_letters))[0] + (day1csv.inputs[i].translate(remove_letters))[-1])
    
#convert list of string to list of int 
listofnumbers = list(map(int, listofnumbers))

sum(listofnumbers)


 

 

 
