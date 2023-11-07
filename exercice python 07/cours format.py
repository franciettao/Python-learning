#vieux
'%10s'%('test')

'{:>10}' .format('test')
#nouveau

print('{:>10}' .format('test'))

#vieux
'%-10s'%('test')

'{:10}' .format('test')
#nouveau

print('{:10}' .format('test'))

#vieux
'%.5s'%('xylophone')

'{:.5}' .format('xylophone')
#nouveau

print('{:.5}' .format('xylophone'))

#vieux
'%d'%(42)

#nouveau
'{:d}' .format(42)

print('{:d}' .format(42))

#INSTALLATION
data={'premier':'Hodor','dernier':'Hodor!'}


#VIEUX
'%(premier)s%(dernier)s'%data

#Nouveau
'{premier}{dernier}'.format(**data)


print('{premier}{dernier}'.format(**data))



#INPUT IF#

# Demandez à l'utilisateur son âge à l'aide de la fonction input()
age_str = input("Veuillez entrer votre âge : ")

try:
    # Convertissez l'entrée en un nombre entier
    age = int(age)

    # Vérifiez si l'âge est dans la plage valide
    if 0 <= age <= 20:
        message = "Jeune"
    elif 20 < age <= 60:
        message = "Adulte"
    elif age > 60:
        message = "Vieux"
    else:
        message = "Erreur : L'âge doit être compris entre 0 et 200."

    # Affichez le message formaté en utilisant .format()
    print("Vous avez {} ans, vous êtes donc un {}.".format(age, message))

except ValueError:
    print("Erreur : Veuillez entrer un âge valide en utilisant un nombre entier.")





#ecrire un programme pour trouver un max entre 3 nombres en utilisant une if-else ou if imbriquée.

entree = 10,16,22
Sortie: 22

num1=int(input("entrer le nombre 1: "))
num2=int(input("entrer le nombre 2: "))
num3=int(input("entrer le nombre 3: "))


if num1 > num2:
    if num1 > num3:

       max =num1

    else:max = num3


else:

    if num2 > Nu

    else


chif1 = int(input("Veuillez entrer votre chiffre1:"))
print (chif1)

chif2 = int(input("Veuillez entrer votre chiffre2:"))
print(chif2)

chif3 = int(input("Veuillez entrer votre chiffre3:"))
print(chif3)

if chif1 > chif2 and chif1 > chif2:
    chifmax = chif1

elif chif2 > chif1 and chif2 > chif3:
    chifmax = chif2

elif chif3 > chif1 and chif3 > chif2:
    chifmax = chif3

print (chifmax)

#________________________________________
#-------------------------------------------------------------------------------


V1 = int(input ("Verifier si un nombre est divisible:"))

if ((V1 % 3 == 0) and (V1 % 13 == 0))

    print(V1, "est divisible par 3 et 13")

else:

    print(V1, "n'est divisible par 3 ni 13")


































