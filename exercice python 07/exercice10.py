#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dell
#
# Created:     07/11/2023
# Copyright:   (c) dell 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

chc=(input("Saisir un caractère : "))[0]

# si ch est une lettre */
if((chc >= 'a' and chc <= 'z') or (chc >= 'A' and chc <= 'Z')):
    print(chc," est une lettre.")
elif(chc >= '0' and chc <= '9'):
    print(chc," est un chiffre.")
else:
    print(chc," est un caractère spéciale.")