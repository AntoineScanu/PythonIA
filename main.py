# Créer les cubes X et Y
from cube import Cube
from robot import Robot
from etat import Etat

cubeA = Cube("A", False, False, True, None)
cubeB = Cube("B", False, True, True, None)
cubeC = Cube("C", False, True, False, cubeA)

# Créer un robot avec un bras vide
robot = Robot(True)

etat = Etat([cubeA, cubeB, cubeC], robot)
etat.afficherEtat()

print("Cube C tenu")
robot.tenir(cubeC)

etat.afficherEtat()

print("Cube C surtable")
robot.poser(cubeC, None)

etat.afficherEtat()

print("Cube B tenu")
robot.tenir(cubeB)

etat.afficherEtat()

print("Cube B sur Cube C")
robot.poser(cubeB, cubeC)

etat.afficherEtat()

print("Cube A tenu")
robot.tenir(cubeA)

etat.afficherEtat()

print("Cube A sur Cube B")
robot.poser(cubeA, cubeB)

print("Etat final")
etat.afficherEtat()


robot.tenir(cubeC)
robot.poser(cubeC, cubeB)
