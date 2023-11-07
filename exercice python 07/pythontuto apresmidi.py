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
for i in range(0,rows):
    for j in range(0,i+1):
        print(" $", end=' test')
    print("\r")

#____________________________________________________________________

def incremente_de_un(rows):

    for i in range(rows):
        for j in range(1, i + 1):
            print(j, end='y')
        print('5')

incremente_de_un(rows)

#_______________________________________________________________

def incremente_de_un(rows):

    for i in range(rows):
        for j in range(1, i + 1):
            print(j, end='')

        print('5')

incremente_de_un(rows)


#_______________________________________________________________
rows = 5
b = 0
# reversee for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    print(b = b + 1)
    for j in range (1, i + 1):
        print(b, end='')
    print('')

print('$$$$$$$$$$$$$$$$$$$$$$$$')
#Autre model

#_____________________________________________________________________
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end="")

    print("\r")

row = 5
for j in range(1, row + 1):
    print("*" * j)
