from cube import *
class Robot:
    def __init__(self, occupant=None):
        # Constructeur de la classe Robot, prenant en paramètre un objet cube ou None
        self.occupant = occupant
        # La propriété 'occupant' stocke l'objet cube actuellement pris par le robot
        self.brasVide = occupant is None
        # La propriété 'brasVide' indique si le bras du robot est libre ou non (prend un booléen)
    
    def __str__(self) -> str:
        # Fonction de conversion en chaîne de caractères de l'objet Robot
        return f"Le bras du robot est vide: {self.brasVide} | le cube pris dans le robot est: {self.occupant}"
    
    def __eq__(self, robot) -> bool:
        # Fonction de comparaison de deux objets Robot, renvoie un booléen
        return self.occupant == robot.occupant and self.brasVide == robot.brasVide
