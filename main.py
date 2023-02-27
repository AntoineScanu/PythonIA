import copy
from tree import *
from cube import *
from robot import *
from noeud import *


# On définit l'heuristique par  rapport au nombre de cube ou d'element dans l'état final :   5 – ( SUR (A,B) + SUR (B,C) + SURTABLE(C) )

def heuristique(noeudActuel):
    surTable = 0
    b_surC = 0
    a_surB = 0

    # boucle à travers tous les cubes de l'état actuel
    for n in noeudActuel.cubes:
        if n.lettre == "C":
            # si le cube est sur la table, ajouter 2 à surTable, sinon soustraire 2
            surTable = 2 if n.surTable else -2
            # si le cube a un cube en dessous et que ce cube est B, ajouter 2 à b_surC, sinon soustraire 2
            b_surC = 2 if n.sous and n.sous.lettre == "B" else -2
        if n.lettre == "A":
            # si le cube a un cube au-dessus et que ce cube est B, ajouter 1 à a_surB, sinon soustraire 1
            a_surB = 1 if n.sur and n.sur.lettre == "B" else -1

    # retourne la somme des valeurs avec un ajustement final de 5
    return 5 - (surTable + b_surC + a_surB)

# Si les conditions sont remplis, on effectue la prochaine operation du bras pour chaque cube du noeud actuel


def genererFils(noeudActuel):
    fils = []
    for i, cube in enumerate(noeudActuel.cubes):
        if cube.surTable and cube.libre and noeudActuel.robot.brasVide:
            # R1
            noeud = copy.deepcopy(noeudActuel)
            noeud.tenirCubeSurTable(noeud.cubes[i])
            noeud.h = heuristique(noeud)
            noeud.pere = noeudActuel
            noeudActuel.fils.append(noeud)
            fils.append(noeud)
            print("R1 : le cube est sur la table et libre, le robot prend le cube")
        elif cube.sur is not None and cube.libre and noeudActuel.robot.brasVide:
            # R2
            noeud = copy.deepcopy(noeudActuel)
            noeud.tenirCubeSurY(noeud.cubes[i])
            noeud.h = heuristique(noeud)
            noeud.pere = noeudActuel
            noeudActuel.fils.append(noeud)
            fils.append(noeud)
            print("R2 : le cube est sur un autre cube et libre, le robot prend le cube")
        elif not noeudActuel.robot.brasVide and noeudActuel.robot.occupant == cube:
            # R3
            noeud = copy.deepcopy(noeudActuel)
            noeud.poseCubeSurTable()
            noeud.h = heuristique(noeud)
            noeud.pere = noeudActuel
            noeudActuel.fils.append(noeud)
            fils.append(noeud)
            print("R3 : Le robot tient un cube et le dépose sur la table")
        elif not noeudActuel.robot.brasVide and noeudActuel.robot.occupant != cube and cube.libre:
            # R4
            noeud = copy.deepcopy(noeudActuel)
            noeud.poseCubeSurCube(noeud.cubes[i])
            noeud.h = heuristique(noeud)
            noeud.pere = noeudActuel
            noeudActuel.fils.append(noeud)
            print("R4 : Le robot tient un cube et le dépose sur un autre cube libre")
            fils.append(noeud)
    return fils


# L'algo A*
# Initialisation des variables ouvert (liste de noeuds à explorer), ferme (liste des noeuds explorés), g (coût de chemin actuel) et it (nombre d'itérations).
def algorithme(noeudRacine, noeudBut):
    # init des tableaux OUVERT et FERME
    ouvert = [noeudRacine]
    ferme = []
    g = 0
    # Tant que OUVERT n'est pas vide
    it = 0
    while len(ouvert) != 0:
        # On met le noeud actuel dans FERME
        noeudActuel = ouvert[0]
        ferme.append(noeudActuel)
        ouvert.remove(noeudActuel)
        print("\nnoeudActuel = "+str(noeudActuel))
        # On génère les différents fils
        successeurs = genererFils(noeudActuel)
        g += 1

        # On vérifie si le noeud but est atteint
        print("noeudsFils :")
        for n in noeudActuel.fils:
            n.g = g
            n.f = n.g + n.h
            print("noeud : h = "+str(n.h)+", g = "+str(n.g))
            if n == noeudBut:
                return n

        # On vérifie si le noeud fils est dans Ouvert||Ferme et on agit
        for n in noeudActuel.fils:

            # Si le fils est dans Ouvert, on compare les 2 occurences
            check = False
            for n2 in ouvert:
                if n2 == n:
                    print('trouvé dans ouvert, on compare les 2')
                    if (n.g < n2.g):
                        ouvert.remove(n2)
                        ouvert.append(n)
                    check = True
                    break
            # Si le fils est dans Ferme, rien ne se passe, on ajoute pas ce noeud dans Ouvert
            if check == False:
                for n2 in ferme:
                    if n2 == n:
                        print('déjà exploré : trouvé dans fermé')
                        check = True
                        break
            # Si le fils n'est ni dans Ouvert ni dans Ferme, on l'ajoute dans Ouvert
            if check == False:
                ouvert.append(n)
        # On trie Ouvert sur F
        ouvert = sorted(ouvert, key=lambda x: x.f)
        it += 1
    return None


def main():
    noeudRacine = buildTree()
    noeudRechercher = noeudBut()

    print('Noeud de départ : \n')
    print(noeudRacine)
    print('Noeud but : \n')
    print(noeudRechercher)
    print(algorithme(noeudRacine, noeudRechercher))
    print("Algorithme realise")


main()
