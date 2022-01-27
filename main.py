"""
Programme Jimini's : manger des insectes comestibles
Salés, sucrés ou naturés, les insectes de chez Jimini's suraont vous régaler tout au long de la journée
"""
from unittest import result
from insecte import Insecte
from boite import Boite

# Programme principal
def afficher(desInsectes) -> None:
    for insecte in desInsectes :
        print(insecte)

def rnjMoyen(lesInsectes) -> None:
    rnjInsecte = 0
    for i in range(len(lesInsectes)):
        insecte = lesInsectes[i]
        rnjInsecte += insecte.getRnj()
    moyenne = rnjInsecte/len(lesInsectes)
    if moyenne == 0 :
        print("La moyenne de rnj est : 0")
    else :
        print("La moyenne de rnj est : ", moyenne)

def afficherBoites(desBoites) -> None:
    for boite in desBoites :
        print(boite)




lesInsectes = []

i1 = Insecte("le criquet", 28)
i2 = Insecte('le grillon', 25)
i3 = Insecte('le molitor', 28)

lesInsectes.append(i1)
lesInsectes.append(i2)
lesInsectes.append(i3)

afficher(lesInsectes)
rnjMoyen(lesInsectes)

lesBoites = [Boite("mangue douce", 10.0, 14, i2), Boite("oignon fumé", 10.0, 14, i2), Boite("paprika", 10.0, 10, i1), Boite("poivre & tomates séchées", 10.0, 10, i1), Boite("curry fruité", 10.0, 10, i1), Boite("à la grecque", 10.0, 10, i1), Boite("sésame & cumin", 10.0, 18, i3), Boite("ail & fines herbes", 10.0, 18,  i3), Boite("soja impérial", 10.0, 18, i3)]
afficherBoites(lesBoites)





# TODO 2 : instancier 3 insectes : le criquet (rnj : 28), le grillon (rnj : 25), le molitor (rnj : 28)
# TODO 3 : ajouter les insectes à la liste d'insectes
# TODO 6 : afficher l'ensemble des insectes (nom)
# TODO 7 : rédiger une fonction rnjMoyen retournant le rnj moyen pour une liste d'insectes fournies en paramètres.
# TODO 8 : tester la fonction rnjMoyen sur la liste d'insecte
