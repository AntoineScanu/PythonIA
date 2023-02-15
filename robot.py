from typing import Optional
from cube import Cube


class Robot:
    def __init__(self, vide: bool):
        self.brasvide = vide

    def tenir(self, cube: Cube):
        cube.estTenu()
        self.brasvide = False

    def poser(self, cube: Cube, support: Optional[Cube] = None):
        if support == None:
            cube.estSurtable()
        else:
            cube.poseSur(support)
        self.brasvide = True
