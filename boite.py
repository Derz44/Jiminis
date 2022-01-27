from insecte import Insecte

class Boite:

    def __init__(self, assaisonnement : str, prix : float, poids : int, unInsecte : Insecte):
        self.__assaisonnement = assaisonnement
        self.__prix = prix
        self.__poids = poids
        self.__linsecte = unInsecte


    def setAssaisonnement(self, valeur : str) -> None:
        self.__assaisonnement = valeur

    def getAssaisonnement(self) -> str:
        return self.__assaisonnement

    def setPoids(self, valeur : int) -> None:
        self.__poids = valeur

    def getPoids(self) -> int:
        return self.__poids

    def setPrix(self, valeur : float) -> None:
        self.__prix = valeur

    def getPrix(self) -> float:
        return self.__prix

    def setlInsecte(self, valeur : Insecte) -> None:
        self.__linsecte = valeur

    def getlInsecte(self) -> Insecte:
        return self.__linsecte

    def __str__(self) -> str:
        return "Boite de " + self.__linsecte.getNom() + " (" + str(self.__poids) + "g) - assaisonnés " + self.__assaisonnement