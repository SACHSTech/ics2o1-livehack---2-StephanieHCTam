"""
-------------------------------------------------------------------------------
Name:     problem1.py
Purpose:  This program determines the martian class of life form detected by Perseverance.

Author:   Tam.S

Created:  23/02/2021
------------------------------------------------------------------------------
"""

print(" ****** Martian Life Detector  ****** ")

# get the number of antenna detected by Perseverance
antennas = int(input("How many antennas? "))

# get the number of eyes detected by Perseverance
eyes = int(input("How many eyes? "))

# compute and output martian class
if antennas >= 3 and eyes <= 4:
  print("Life form detected: AudreyMartian")
if antennas <= 6 and eyes >= 2:
  print("Life form detected: MaxMartian")
if antennas <= 2 and eyes <= 3:
  print("Life form detected: BrooklynMartian")
if antennas == 0 and eyes == 2:
  print("Life form detected: MattDamonMartian")
  
else:
  print("No life form detected.")