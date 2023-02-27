class Cube:
    def __init__(self, lettre, surTable=True, sur=None):
        # Initialisation des attributs de la classe
        self.lettre = lettre # lettre associée au cube
        self.surTable = surTable # indique si le cube est sur la table ou non
        self.sur = sur # cube sur lequel est posé le cube actuel
        self.libre = True # indique si le cube est libre ou non
        self.sous = None # cube posé sur le cube actuel

        # Vérification si le cube est posé sur un autre cube ou non
        if sur is not None: 
            # Si le cube est posé sur un autre cube
            self.sur = sur # on définit le cube sur lequel est posé le cube actuel
            self.surTable = False # le cube n'est plus sur la table
            sur.sous = self # le cube actuel est posé sur le cube sur lequel il est posé
            sur.libre = False # le cube sur lequel est posé le cube actuel n'est plus libre

  
    def mettreSur(self, cube):
    #Met le cube actuel sur un autre cube
        self.sur = cube
        cube.sous = self
        cube.libre = False

    def __str__(self):
    #Retourne une chaîne de caractères décrivant le cube
        if self.sur is None:
            sur_cube = 'table'
        else:
           sur_cube = self.sur.lettre
        if self.libre:
            libre = 'libre'
        else:
            libre = 'occupe'
        return f'Cube {self.lettre} ({libre}), sur {sur_cube}'

    def __eq__(self, other):
        # Vérifie si l'objet other est bien un Cube
        if not isinstance(other, Cube):
            return False
        # Vérifie l'égalité des lettres, de la position sur table et de la position sur un autre cube
        return (self.lettre == other.lettre and self.surTable == other.surTable and self.sur == other.sur)
