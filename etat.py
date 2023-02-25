from cube import Cube
from robot import Robot

from typing import List


class Etat:
    def __init__(self, cubes: dict, robot: Robot):
        self.cubes = cubes
        self.robot = robot

    def ajouterCube(self, cube):
        self.cubes.append(cube)

    def supprimerCube(self, cube):
        self.cubes.remove(cube)

    def afficherEtat(self):
        for nom, cube in self.cubes.items():
            cube.afficherCube()
        print("Robot bras vide : " + str(self.robot.brasvide))
        print('-------------------------')
