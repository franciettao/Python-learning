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

import math
pf=float(input("Prix de fabrication : "))
pv=float(input("Prix de vente : "))
montant = abs(pv - pf)
if(pv >= pf):
    # calculer profit /
    print("Profit = ", montant)
else:
     # calculer la perte/
    print("Perte = ", montant)