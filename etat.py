from cube import Cube
from robot import Robot

from typing import List


class Etat:
    def __init__(self, cubes: List[Cube], robot: Robot):
        self.cubes = cubes
        self.robot = robot

    def ajouterCube(self, cube):
        self.cubes.append(cube)

    def supprimerCube(self, cube):
        self.cubes.remove(cube)

    def afficherEtat(self):
        for c in self.cubes:
            c.afficherCube()
        print("Robot : " + str(self.robot.brasvide))
        print('-------------------------')
