from os import system
import sys
system("cls")

print("Application de Gestion pharmaceutique (Stock et Vente)")
name = input("Entrer votre nom: ")
print('Salut '+name)
print('Bienvenue dans ton espace de travail :)')
Q = input("Are you going to access the 'Vente space' or 'Stock space'? ")
def click():
    while Q != 'Vente space' or Q != 'Stock space': #Tjs ecrire l'inverse dans la condition "While"
        if Q == 'Vente space':
            print("Vente Space Open!")
            nbr_items = int(input('Entrer le nombre de produits acheter par le client: '))
            T = []
            b = []
            i = 0
            prix = 0
            for i in range(nbr_items):
                datum = (str(input('Enter le nom du produit: ')), int(input('Enter ID: ')))
                nbr_produit = int(input("Entrer la quantite du produit! : "))
                prix = float(input('Enter prix: '))
                somme = int(nbr_produit) * float(prix)
                b.append(somme)
            for j in range(nbr_items):
                s = sum(b)
                print('Les prix calculer pour chaque produits est => ')
                print(b)
                print('La somme total est ' + str(s)+ ' Dh')
            break
        elif Q == 'Stock space':
                print("Stock Space Open!")
                print("Please choose Between : ")
                print('"Add" a new product')
                print('"Delete" a product')
                print('"Alter" a product')
                Q1 = input("=>")
        
        else:
            print("Vous avez pu avoir une erreur dans la saisie de votre reponse. Veuillez réessayer SVP!")
            Q = input("Are you going to access the 'Vente space' or 'Stock space'? ")
