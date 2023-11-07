#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      dell
#
# Created:     07/11/2023
# Copyright:   (c) dell 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end="")

    print("\r")

row = 5
for j in range(1, row + 1):
    print("*" * j)
