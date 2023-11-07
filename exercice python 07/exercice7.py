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
#afficher le nombre de mois entre 1 et 12

mois = int(input("Entrer numero du mois entre (1 et 12):"))

#afficher le nombre de jours de ce mois avec if-else
if mois == 1:
    print('31 jours')

elif mois == 2:
    print ('28-29 jours')

elif mois == 3:
    print ('31 jours')

elif mois == 4:
    print ('30 jours')

elif mois == 5:
    print ('31 jours')

elif mois == 6:
    print ('30 jours')

elif mois == 7:
    print ('31 jours')

elif mois == 8:
    print ('31 jours')

elif mois == 9:
    print ('30 jours')


elif mois == 10:
    print ('31 jours')

elif mois == 11:
    print ('30 jours')

elif mois == 12:
    print ('31 jours')

else:
    print ("Mois invalider" "Veuillez saisir le numéro du mois entre (1-12).")



# Créez un dictionnaire de correspondance entre les numéros de mois et les noms de mois
noms_des_mois = {
    1: "Janvier",
    2: "Février",
    3: "Mars",
    4: "Avril",
    5: "Mai",
    6: "Juin",
    7: "Juillet",
    8: "Août",
    9: "Septembre",
    10: "Octobre",
    11: "Novembre",
    12: "Décembre"
}

# Demandez à l'utilisateur de saisir le numéro du mois entre 1 et 12
mois = int(input("Entrez le numéro du mois entre (1 et 12) : "))

# Utilisez une structure if-else pour afficher le nombre de jours et le nom du mois
if mois in noms_des_mois:
    nom_du_mois = noms_des_mois[mois]
    if mois == 2:
        print(f"{nom_du_mois} a 28 ou 29 jours")
    elif mois in [4, 6, 9, 11]:
        print(f"{nom_du_mois} a 30 jours")
    else:
        print(f"{nom_du_mois} a 31 jours")
else:
    print("Mois invalide. Veuillez saisir le numéro du mois entre (1-12).")


