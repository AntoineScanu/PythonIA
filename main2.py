import copy
from tree import *
from cube import *
from robot import *
from noeud import *

#Pour chaque etat du noeud final non rempli, on ajoute 1
def heuristique(noeudActuel):
    count = 0
    
    for n in noeudActuel.cubes:
        if n.lettre == "A":
            if n.libre == False:
                count += 1
            if n.sur != None:
                if n.sur.lettre != "B":
                    count += 1
            else:
                count += 1
        if n.lettre == "B":
            if n.libre == True:
                count +=1
            if n.sur != None:
                if n.sur.lettre != "C":
                    count += 1
            else:
                count += 1
        if n.lettre == "C":
            if n.libre == True:
                count +=1
            if n.surTable == False:
                count += 1
    
    if noeudActuel.robot.brasVide == False:
        count += 1
    
    return count


#Pour chaque cube du noeudActuel, si certaines conditions sont remplies, on effectue l'opération du robot et on crée le nouveau noeud
def genererFils(noeudActuel):
    fils = []
    
    #for n in noeudActuel.cubes:
    i = 0
    while i < len(noeudActuel.cubes):
        #R1
        if(noeudActuel.cubes[i].surTable == True and noeudActuel.cubes[i].libre == True and noeudActuel.robot.brasVide == True):
            noeud = copy.deepcopy(noeudActuel)
            noeud.tenirCubeSurTableR1(noeud.cubes[i])
            noeud.h = heuristique(noeud)
            noeud.pere = noeudActuel
            noeudActuel.fils.append(noeud)
            fils.append(noeud)
            print("R1")
            #print(noeud)
        #R2
        if(noeudActuel.cubes[i].sur != None and noeudActuel.cubes[i].libre == True and noeudActuel.robot.brasVide == True):
            noeud = copy.deepcopy(noeudActuel)
            noeud.tenirCubeSurYR2(noeud.cubes[i])
            noeud.h = heuristique(noeud)
            noeud.pere = noeudActuel
            noeudActuel.fils.append(noeud)
            fils.append(noeud)
            print("R2")
        #R3
        if(noeudActuel.robot.brasVide == False and noeudActuel.robot.occupant == noeudActuel.cubes[i]):
            noeud = copy.deepcopy(noeudActuel)
            noeud.poseCubeSurTableR3()
            noeud.h = heuristique(noeud)
            noeud.pere = noeudActuel
            noeudActuel.fils.append(noeud)
            fils.append(noeud)
            print("R3")
        #R4
        if(noeudActuel.robot.brasVide == False and noeudActuel.robot.occupant != noeudActuel.cubes[i]):
            if(noeudActuel.cubes[i].libre == True):
                noeud = copy.deepcopy(noeudActuel)
                noeud.poseCubeSurCubeR4(noeud.cubes[i])
                noeud.h = heuristique(noeud)
                noeud.pere = noeudActuel
                noeudActuel.fils.append(noeud)
                print("R4")
        i += 1
   
    return fils

#Algo A*
def algorithme(noeudRacine,noeudBut):
    #init des tableaux OUVERT et FERME
    ouvert = [noeudRacine]
    ferme = []
    g = 0
    #Tant que OUVERT n'est pas vide
    it = 0
    while len(ouvert) != 0:
        #On met le noeud actuel dans FERME
        noeudActuel = ouvert[0]
        ferme.append(noeudActuel)
        ouvert.remove(noeudActuel)
        print("\nnoeudActuel = "+str(noeudActuel))
        #On génère les différents fils
        successeurs = genererFils(noeudActuel)
        g += 1
    
        #On vérifie si le noeud but est atteint
        print("noeudsFils :")
        for n in noeudActuel.fils:
            n.g = g
            n.f = n.g + n.h
            print("noeud : h = "+str(n.h)+", g = "+str(n.g))
            if n == noeudBut:
                return n
            
        #On vérifie si le noeud fils est dans Ouvert||Ferme et on agit
        for n in noeudActuel.fils:
            
            #Si le fils est dans Ouvert, on compare les 2 occurences
            check = False
            for n2 in ouvert:
                if n2 == n:
                    print('trouve ds ouvert')
                    if(n.g < n2.g):
                        ouvert.remove(n2)
                        ouvert.append(n)
                    check = True
                    break
            #Si le fils est dans Ferme, rien ne se passe, on ajoute pas ce noeud dans Ouvert
            if check == False:
                for n2 in ferme:
                      if n2 == n:
                        print('trouve ds ferme')
                        check = True
                        break
            #Si le fils n'est ni dans Ouvert ni dans Ferme, on l'ajoute dans Ouvert
            if check == False:
                ouvert.append(n)
        #On trie Ouvert sur F
        ouvert = sorted(ouvert, key=lambda x: x.f)
        it += 1  
    return None


def main() :
    noeudRacine = buildTree()
    print('Noeud de départ : \n')
    print(noeudRacine)
    print('Noeud but : \n')
    noeudRechercher = noeudBut()
    print(noeudRechercher)
    print(algorithme(noeudRacine,noeudRechercher))
    print("Algorithme realise !")

    
main()