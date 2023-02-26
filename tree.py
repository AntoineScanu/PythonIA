from robot import *
from cube import *
from noeud import *

# Cette fonction construit un arbre contenant trois cubes et un robot
# Le robot commence avec un bras vide et deux des trois cubes sont sur la table
# Le troisième cube est posé sur le premier cube
def buildTree():
    robot = Robot()
    cubeA = Cube("A", True, None)
    cubeB = Cube("B", True, None)
    cubeC = Cube("C", False, cubeA)
    
    return Noeud(robot, [cubeA, cubeB, cubeC])

# Cette fonction crée un noeud représentant l'état final que l'on souhaite atteindre
# Le robot commence avec un bras vide et tous les cubes sont empilés dans l'ordre inverse sur la table
def noeudBut():
    robot = Robot()
    
    cubeC = Cube("C", True, None)
    cubeB = Cube("B", False, cubeC)
    cubeA = Cube("A", False, cubeB)
    
    return Noeud(robot, [cubeA, cubeB, cubeC])

