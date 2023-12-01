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


 

 

 
