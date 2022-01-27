from boite import Boite

class Catalogue :
    def __init__(self, saison : str, lesBoites : Boite ):
        self.__saison = saison
        self.__lesBoites = lesBoites

    def setSaison(self, valeur : str) -> str :
        self.__saison = valeur

    def getSaison