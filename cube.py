class Cube:
    def __init__(self, nom: str, tenu: bool, libre: bool, surtable: bool, cube: 'Cube'):
        self.nom = nom
        self.tenu = tenu
        self.libre = libre
        self.surtable = surtable
        self.sur = cube

    def estTenu(self):
        self.tenu = True
        self.libre = False
        self.surtable = False
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
        self.sur = cube
        cube.libre = False

    def afficherCube(self):
        cube = "Cube " + self.nom + \
            " [tenu: " + str(self.tenu) + " , libre: " + str(self.libre) + \
            ", surtable: " + str(self.surtable) + ", sur: "

        if self.sur == None:
            cube += "Table"
        else:
            cube += self.sur.nom

        cube += "]"

        print(cube)
