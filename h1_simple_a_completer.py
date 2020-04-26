import game
import random
from functools import reduce
moi=1
nbNoeuds=0
params=[10,1]

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    j=game.getJoueur(jeu)
    global moi
    moi=j
    global scores
    scores=game.getScores(jeu)
    l=game.getCoupsValides(jeu)
    return decision(jeu,l)


def decision(jeu,listCoups):
    """ jeu * List[coup] -> coup
        Decide d'un coup a jouer
    """
    m=-10000000000
    imax=None
    for x in listCoups:
        v=estimation(jeu,x,1)
        if(v>m):
            m=v
            imax=x
    return imax

def estimation(jeu,coup,prof):
    """ jeu * coup * prof -> number
        Estime la valeur d'un coup
    """
    
    global nbNoeuds
    
    nbNoeuds+=1
    copie=game.getCopieJeu(jeu)
    game.joueCoup(copie,coup)
    
    if(game.finJeu(copie)):
        #A Completer
        
    return evaluation(copie)

    
def evaluation(jeu):
    """ jeu->number
        evalue une situation de jeu pour le joueur moi
    """
    l=getEvals(jeu)
    return dotProduct(l,params)
    

def dotProduct(l1,l2):
    #A Completer
    

def getEvals(jeu):
    return [evalScores(jeu),evalPos(jeu)]

def evalScores(jeu):
    """ jeu -> List[number}
        evalue une situation de jeu en faisant la difference entre le score de moi et le score de l'adversaire
    """
    autre=moi%2+1
    sc=game.getScores(jeu)
    return sc[moi-1]-sc[autre-1]


def evalPos(jeu):
    diffExtr = 0
    
    p = 0.8
    plateau=game.getPlateau(jeu)
    j1=0
    j2=0
    ligne=plateau[0]
    ligne2=plateau[1]
    for i in range(6):
        j1 += p * ligne[i]
        j2 += p * ligne2[-i-1]
        p-=0.1

    diffExtr=j1-j2
    if(moi==2):
       diffExtr=-diffExtr
       
    return diffExtr





