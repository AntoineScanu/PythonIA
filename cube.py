class Cube:
    def __init__(self, nom: str, tenu: bool, libre: bool, surtable: bool, sur: str):
        self.nom = nom
        self.tenu = tenu
        self.libre = libre
        self.surtable = surtable
        self.sur = sur

    def estTenu(self, etat):
        self.tenu = True
        self.libre = False
        self.surtable = False
        if self.sur != None:
            etat.cubes[self.sur].libre = True
        else:
            self.sur = None

    def estSurtable(self):
        self.tenu = False
        self.libre = True
        self.surtable = True
        self.sur = None

    def poseSur(self, cube: 'Cube'):
        self.tenu = False
        self.libre = True
        self.surtable = False
        self.sur = cube.nom
        cube.libre = False

    def afficherCube(self):
        cube = "Cube " + self.nom + \
            " [tenu: " + str(self.tenu) + " , libre: " + str(self.libre) + \
            ", surtable: " + str(self.surtable) + ", sur: "

        if self.sur == None and self.tenu == False:
            cube += "Table"
        elif self.tenu == True:
            cube += "Rien"
        else:
            cube += self.sur

        cube += "]"

        print(cube)
