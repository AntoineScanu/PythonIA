from cube import Cube
from robot import Robot
from etat import Etat


def g1(g):
    return g


def h1(e):
    h = 5
    if e.cubes["C"].surtable:
        h -= 1
    if e.cubes["A"].libre:
        h -= 1
    if e.cubes["B"].sur == e.cubes["C"]:
        h -= 1
    if e.cubes["A"].sur == e.cubes["B"]:
        h -= 1
    if e.robot.brasvide:
        h -= 1

    return h


def afficherGH(cube, e, g):
    print('Cube : ' + cube.nom)
    print('h : ' + str(h1(e)))
    print('g : ' + str(g1(g)))
    print('------')


g = 0
cubeA = Cube("A", False, False, True, None)
cubeB = Cube("B", False, True, True, None)
cubeC = Cube("C", False, True, False, "A")
cubes = {"A": cubeA, "B": cubeB, "C": cubeC}

cubeCFinal = Cube("C", False, False, True, None)
cubeBFinal = Cube("B", False, False, False, "C")
cubeAFinal = Cube("A", False, True, False, "B")
cubesFinal = {"A": cubeAFinal, "B": cubeBFinal, "C": cubeCFinal}

robot = Robot(True)
etat = Etat(cubes, robot)
etatFinal = Etat(cubesFinal, robot)
arbre = []

ouvert = []
ferme = []

# while h1() != 0:
if robot.brasvide:
    for cube in etat.cubes.values():
        if cube.libre:
            ouvert.append(cube)

    for cube in ouvert:
        gTemp = g
        cubeATemp = Cube(cubeA.nom, cubeA.tenu, cubeA.libre,
                         cubeA.surtable, cubeA.sur)
        cubeBTemp = Cube(cubeB.nom, cubeB.tenu, cubeB.libre,
                         cubeB.surtable, cubeB.sur)
        cubeCTemp = Cube(cubeC.nom, cubeC.tenu, cubeC.libre,
                         cubeC.surtable, cubeC.sur)
        robotTemp = Robot(robot.brasvide)
        etatTemp = Etat({"A": cubeATemp, "B": cubeBTemp,
                        "C": cubeCTemp}, robotTemp)
        robotTemp.tenir(etatTemp.cubes[cube.nom], etatTemp)
        gTemp += 1
        afficherGH(cube, etatTemp, gTemp)
        f = h1(etatTemp) + g1(gTemp)
        print("f : " + str(f))
        # if h1(etatTemp) + g1(g) > f
