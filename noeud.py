from cube import *

class Noeud:
    def __init__(self, robot, cubes, h=5, g=0, pere=None):
        # Initialisation des attributs de la classe
        self.robot = robot
        self.cubes = cubes
        self.h = h
        self.g = g
        self.f = self.g + self.h
        self.pere = pere
        self.fils = []
        
        # Si le noeud a un père, on l'ajoute à la liste des fils de ce père
        if pere is not None:
            pere.fils.append(self)
    
    def tenirCubeSurTable(self, cube):
        # Le robot saisit le cube
        self.robot.occupant = cube
        self.robot.brasVide = False
    
        # Le cube n'est plus sur la table et n'est plus libre
        cube.surTable = False
        cube.libre = False
    
        # On met à jour la liste des cubes
        for n in self.cubes:
            if n.lettre == cube.lettre:
                n=cube

        
    def tenirCubeSurY(self, cube):
        # Le robot prend le cube 
        self.robot.occupant = cube
        self.robot.brasVide = False
        
        # Le cube n'est plus supporté par son support Y
        cube.sur.libre = True
        cube.sur.sous = None
        cube.sur = None
        
        # Le cube n'est plus libre car il est maintenu par le robot
        cube.libre = False
        
        # On met à jour la liste des cubes pour refléter le nouvel état du cube
        for n in self.cubes:
            if n.lettre == cube.lettre:
                n = cube
                break

        
    def poseCubeSurTable(self):
        self.robot.occupant.surTable = True
        self.robot.occupant.libre = True
        self.robot.occupant = None
        self.robot.brasVide = True

    
    def poseCubeSurCube(self, CubeY):
        self.robot.occupant.libre = True
        self.robot.occupant.mettreSur(CubeY)
        self.robot.occupant = None
        self.robot.brasVide = True



    def __str__ (self) -> str:
         res  ='Etat du robot : '+str(self.robot)+'\n'
         res = res + 'h : '+str(self.h)+' | g : '+str(self.g)+' | f : '+str(self.f)+'\n'
         res = res +'\nCubes : \n'
         for c in self.cubes:
             res = res + str(c)+'\n'
         return res
        
    def __eq__(self,noeud2) -> bool : 
        if (isinstance(noeud2, Noeud)):
            if(not(self.robot == noeud2.robot)):
                return False
            for n in self.cubes:
                check = False
                for n2 in noeud2.cubes:
                    if(n == n2):
                        check = True
                        break
                if(check == False):
                    return False
            return True
        return False