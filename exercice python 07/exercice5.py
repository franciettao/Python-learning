#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      dell
#
# Created:     07/11/2023
# Copyright:   (c) dell 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


v1 = "lundi"
v2 = "mardi"
v3 = "mercredi"
v4 = "jeudi"
v5 = "vendredi"
v6 = "samedi"
v7 = "dimanche"

# Demandez à l'utilisateur de saisir le nom du jour de la semaine
jour_de_la_semaine = input("Entrez le nom du jour de la semaine : ")

# Utilisez une structure if-else pour afficher le jour correspondant
if jour_de_la_semaine == v1:
    print("Lundi")
elif jour_de_la_semaine == v2:
    print("Mardi")
elif jour_de_la_semaine == v3:
    print("Mercredi")
elif jour_de_la_semaine == v4:
    print("Jeudi")
elif jour_de_la_semaine == v5:
    print("Vendredi")
elif jour_de_la_semaine == v6:
    print("Samedi")
elif jour_de_la_semaine == v7:
    print("Dimanche")
else:
    print("Jour de la semaine invalide. Veuillez entrer un nom de jour valide.")