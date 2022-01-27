class Insecte:
    """Classe Insecte
    Permet de créer une instance d'Insecte
    Attributs d'instance
    --------------------
    nom : str
        nom de l'animal
    rnj : int
        repère nutritionnel journalier (rnj) correspondant à la teneur en énergie et en macro-nutriments.
    """

    def __init__(self, unNom : str, valRnj : int):
        self.setNom(unNom)
        self.__rnj = valRnj

        """Constructeur de la classe Insecte
        """



        #TODO 1: implémenter le constructeur de la classe

    def getNom(self) -> str:
        """Getter sur l'attribut nom
        :return: str, le nom de l'insecte
        """
        return self.__nom

    def setNom(self, valeur : str) -> None :
        """Setter sur l'attribut nom
        :param valeur : valeur pour le nom
        """
        self.__nom = valeur

    def getRnj(self) -> int:
        return self.__rnj

    def setRnj(self, valeur : int) -> None :
        self.__rnj = valeur

    def __str__(self) -> str:
        resultat = self.__nom + " (valeur nutritionnelle de : " + str(self.__rnj) + ")"
        return resultat




    #TODO 4 : implémenter les méthodes get et set pour l'attribut rnj

    #TODO 5: définir la méthode permettant de générer l'affichage d'une instance d'Insecte au format str
