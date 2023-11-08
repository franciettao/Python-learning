#-------------------------------------------------------------------------------
# Name: cours listes
# Purpose: Python
#
# Author:      Olivier
#
# Created:     08/11/2023
# Copyright:   (c) dell 2023
# Licence:     Ingenieur Devops
#------------------------------------------------------------------------------




liste_1 =[]

liste_2 =list()

print(liste_1,liste_2)



exemple_liste =[8.9,"kevin"]
print(exemple_liste)


#non mutable non calable
tuple_prenoms = ("Gustave","Solange","Alphonse")
liste_prenoms= list(tuple_prenoms)
print(liste_prenoms)

resultat: ["Gustave", 'Solange', 'Alphonse']

#methode append ()
#vous pouvez ajouter des éléments qui seront affectés à la fin de la liste
exemple_liste=[8,6.9,"kevin"]
exemple_liste.append("loana")
exemple_liste.append("kim")
exemple_liste.append('olivier')
print(exemple_liste)

#fonction intégréé len()
#retourne un entier qui correspon au nombre entier d'elements contenu dans la liste
print(len(exemple_liste))

#Je place de l'indice de l'élément recherché entre crochets
#indicé a partir de 0#
element=exemple_liste[2]
print(element)


#methode insert()

#methode inster permet intercaler un nouvel element:

exemple_liste.insert(1,"Gabrielle")
print(exemple_liste)

exemple_liste.insert(4,"Mikasa")
print(exemple_liste)

exemple_liste.insert(5,"Monster")
print(exemple_liste)

exemple_liste.insert(-1,"Jojo")
print(exemple_liste)

exemple_liste.insert(-2,"Joana")
print(exemple_liste)

#methode extend()


jours=["Lundi","mardi","mercredi"]
jours2=["Jeudi","Vendredi"]
jours.extend(jours2)
print(jours)

jours2.extend(jours)
print(jours2)


jours=["Lundi","mardi","mercredi"]
jours2=["Jeudi","Vendredi"]
jours.append(jours2)
print(jours)

#sous liste
#mehotde 1

jours=["Lundi","mardi","mercredi",["Jeudi", "vendredi"]]
#je place indice entre crochet
element= jours[2]
print(element)


#methode 2

jours=["Lundi","mardi","mercredi",["Jeudi", "vendredi"]]
#je place indice element rechercher entre crochet
element= jours[3][1]
print(element)

 #3 dans la list principal
 #1 petite liste ou sous liste


#slicing pour modifier une liste


jours=["Lundi","Mardi","Jeudi"]
#je souhaite inserer "Mercredi"
jours[2:2]=["mercredi"]
print(jours)



jours=["Lundi","Mardi","Jeudi"]
#je souhaite inserer "Mercredi"
jours[0:1]=["mercredi"]
print(jours)

#warning#--------------------------------------

jours=["Lundi","Mardi","Jeudi"]
#je souhaite inserer "Mercredi"
jours[2:2]="mercredi"
print(jours)
#warning#---------------------------------------


prenoms=['Gabrielle','Alphonse','kevin','loana']
print(prenoms[1:3])

prenoms=['Gabrielle','Alphonse','kevin','loana']
print(prenoms[2:4])

prenoms=['Gabrielle','Alphonse','kevin','loana']
print(prenoms[3:3])

prenoms=['Gabrielle','Alphonse','kevin','loana']
print(prenoms[1:4])


"""prenoms = ['Gabrielle', 'Alphonse', 'Kevin', 'Loana']

prenoms[:] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']
# Cela remplace la liste entière par la nouvelle liste fournie.

prenoms[1:] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']
# Cela remplace tous les éléments à partir de l'indice 1 par la nouvelle liste.

prenoms[:-1] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']
# Cela remplace tous les éléments sauf le dernier par la nouvelle liste.

prenoms[:-2] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']
# Cela remplace tous les éléments sauf les deux derniers par la nouvelle liste.

prenoms[-1] = prenoms[3] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']

prenoms[::2] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']
# Cela remplace chaque deuxième élément par la nouvelle liste.

prenoms[::3] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']
# Cela remplace chaque troisième élément par la nouvelle liste.

prenoms[::-1] =['Gabrielle', 'Alphonse', 'Kevin', 'Loana']
# Cela inverse l'ordre des éléments de la liste."""

prenoms = ["Gabriel","Alphonese", "kevin", "loana"]
print(prenoms[1:3])
print(prenoms[:]) #Liste entiere
print(prenoms[1:])
print(prenoms[:-1])
print(prenoms[:-2])
print(prenoms[-1])
print(prenoms[::2])
print(prenoms[::3])
print(prenoms[::-1]) #inverseles élements


#methode associees aux objets de type list ()

"""il est exist list.sort()"""

prenoms= ["Gabriel","Alphonese", "kevin", "loana"]
nombres= [8,52,0,3.2,-5.6,7,-23]
prenoms.sort()
nombres.sort()
print(prenoms)
print(nombres)

"""list.sort ()  reverse=True."""

prenoms= ["Gabriel","Alphonese", "kevin", "loana"]
nombres= [8,52,0,3.2,-5.6,7,-23]
prenoms.sort(reverse=True)
nombres.sort(reverse=True)
print(prenoms)
print(nombres)


"""list.index() list.index(element) est une méthode en Python qui renvoie
l'indice de la première occurrence de l'élément spécifié dans la liste.
 Si l'élément n'est pas trouvé, une erreur ValueError est déclenchée."""

"""prenoms= ["Gabriel","Alphonese", "kevin", "loana"]
nombres= [8,52,0,3.2,-5.6,7,-23]
i=prenoms.index('Gabriel')
i2=nombres.index(53)
print(i)
print(i2)"""

prenoms= ["Gabriel","Alphonese", "kevin", "loana", "Gabriel"]
nombres= [8,52,0,3.2,-5.6,7,-23]
i=prenoms.index('Gabriel',3)
print(i)

"""resultat 4: (la premiere valeur "Gabrielle" est ignorée)"""

"""list.reverse"""

prenoms= ["Gabriel","Alphonese", "kevin", "loana"]
prenoms.reverse()
print(prenoms)

prenoms= ["Gabriel","Alphonese", "kevin", "loana"]
popped=prenoms.pop(1)
print(popped,prenoms)


"""list.remove()"""

prenoms= ["Gabriel","Alphonese", "kevin", "loana", "kevin"]
prenoms.remove("kevin")
print(prenoms)

prenoms= ["Gabriel","Alphonese", "kevin", "loana", "kevin"]
prenoms.remove("loana")
print(prenoms)

"""list.count()"""

prenoms= ["Gabriel","Alphonese", "kevin", "loana", "kevin"]
n = prenoms.count("kevin")
print(n)

prenoms= ["Gabriel","Alphonese", "kevin", "loana", "kevin"]
n = prenoms.count("kim")
print(n)

"""list du test d'appartenance

ma_liste = [1, 2, 3, 4, 5]
element = 3

if element in ma_liste:
    print("L'élément appartient à la liste.")
else:
    print("L'élément n'appartient pas à la liste.")
Dans cet exemple, nous vérifions si l'élément 3 appartient à la liste ma_liste en utilisant l'opérateur in.
Vous pouvez personnaliser element avec la valeur que vous souhaitez vérifier."""

"""ma_liste = [1, 2, 3, 4, 5]
element_recherche = int(input("Entrez l'élément à rechercher : "))

if element_recherche in ma_liste:
    print("L'élément appartient à la liste.")
else:
    print("L'élément n'appartient pas à la liste.")"""


prenoms= ["Gabriel","Alphonese", "kevin", "loana"]
result ='Baptiste' in prenoms #Retourne un boleen(True ou False)
print(result)


prenoms= ["Gabriel","Alphonese", "kevin", "loana"]
result ='Baptiste' in prenoms #Retourne un boleen(True ou False)
if result in prenoms:
    print("L'élément est True.")
else:
    print("L'élément est False")


prenoms = ["Gabriel", "Alphonse", "Kevin", "Loana"]
element_recherche = "Baptiste"

try:
    if element_recherche in prenoms:
        print("L'élément est True.")
    else:
        print("L'élément est False.")
except:
    print("Une erreur s'est produite.")
finally:
    print("Fin du programme.")


prenoms = ["Gabriel", "Alphonse", "Kevin", "Loana"]
element_recherche = input("Entrez l'élément à rechercher : ")

try:
    if element_recherche in prenoms ():
        print("L'élément est True.")
    else:
        print("L'élément est False.")
except:
    print("Une erreur s'est produite.")
finally:
    print("Fin du programme;")






