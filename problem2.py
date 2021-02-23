"""
-------------------------------------------------------------------------------
Name:     problem2.py
Purpose:  This program determines whether the figure is a triangle or not. 

Author:   Tam.S

Created:  23/02/2021
------------------------------------------------------------------------------
"""

print("Welcome to the Triangle Checker")

# get side lengths of triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# determine and output if sides make a triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1): 
  print("The figure is a triangle.")
else:
  print("The figure is NOT a triangle.")