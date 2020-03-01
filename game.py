#!/usr/bin/env python
# -*- coding: utf-8 -*-

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2

class plateau:
	# plateau: List[List[nat]]
	# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

	def __init__(self, nbLigne, nbColonne):
		# Creation du plateau
		# Et initialisation a 0
		self.plateau = []
		for l in range (nbLigne):	
			self.plateau.append([])
			for c in range (nbColonne):
				self.plateau[l].append(0)

class coup:
	# coup:[nat nat]
	# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur
	
	def __init__(self, nbLignes, nbColonnes):
		self.ligne = nbLignes
		self.colonne = nbColonnes

class Jeu:
	# Jeu
	# jeu:[plateau nat List[coup] List[coup] List[nat nat]]
	# Structure de jeu comportant :
	#           - le plateau de jeu
	#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
	#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
	#           - La liste des coups joues jusqu'a present dans le jeu
	#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2
	
	def __init__(self, nbL, nbC, liste_coups_joues, liste_coups_possibles, QuelJoueur, liste_scores):
		self.plat = plateau(nbL, nbC)
		self.coups_joues = liste_coups_joues
		self.coups_possibles = liste_coups_possibles
		self.joueur = QuelJoueur
		self.scores = liste_scores


#Fonctions minimales 

def getCopieListe(liste):
	"""liste->liste
		retourne une copie de la liste entree en parametre
	"""
	new_liste = []
	for e in liste:
		new_liste.append(e)
	return new_liste

def getCopieListeCoups(listeCoups):
	"""liste de Coups -> liste de Coups
		retourne une copie de la liste de coups entree en parametre
	"""
	new_listeCoups = []
	for c in listeCoups:
		new_listeCoups.append(coup(c.ligne, c.colonne))
	return new_listeCoups

def getCopiePlateau(Plateau):
	"""plateau->plateau
		retourne une copie du plateau entree en parametre
	"""
	nbL = game.lignes
	nbC = game.colonnes
	new_plateau = plateau(nbL, nbC)
	for l in range(nbL):
		for c in range(nbC):
			new_plateau.plateau[l][c] = Plateau.plateau[l][c]
	return new_plateau

def getCopieJeu(jeu):
	""" jeu->jeu
		Retourne une copie du jeu passe en parametre
		Quand on copie un jeu on en calcule forcement les coups valides avant
	"""
	new_jeu = initialiseJeu()
	#new_jeu.plateau = getCopiePlateau(jeu.plat)
	for l in range(game.lignes):
		for c in range(game.colonnes):
			new_jeu.plat.plateau[l][c] = jeu.plat.plateau[l][c]
	new_jeu.coups_joues = getCopieListeCoups(jeu.coups_joues)
	if (jeu.coups_possibles[0] != None):
		new_jeu.coups_possibles = getCopieListeCoups(jeu.coups_possibles)
	else:
		new_jeu.coups_possibles = [None]
	new_jeu.joueur = jeu.joueur
	new_jeu.scores = getCopieListe(jeu.scores)
	return new_jeu

def finJeu(jeu):
	""" jeu -> bool
		Retourne vrai si c'est la fin du jeu
	"""
	return game.finJeu(jeu)

def saisieCoup(jeu):
	""" jeu -> coup
		Retourne un coup a jouer
		On suppose que la fonction n'est appelee que si il y a au moins 
		un coup valide possible et qu'elle retourne obligatoirement un coup valide
	"""
	if (jeu.joueur == 1):
		return joueur1.saisieCoup(jeu)
	return joueur2.saisieCoup(jeu)

def getCoupsValides(jeu):
	""" jeu  -> List[coup]
		Retourne la liste des coups valides dans le jeu passe en parametre
		Si None, alors on met � jour la liste des coups valides
	"""
	if (jeu.coups_possibles == [None]):
		jeu.coups_possibles = game.getCoupsValides(jeu)
		return jeu.coups_possibles
	return jeu.coups_possibles
		

def coupValide(jeu,coup):
	"""jeu*coup->bool
		Retourne vrai si le coup appartient a la liste de coups valides du jeu
	"""
	for Coup in jeu.coups_possibles:
		if (Coup.ligne == coup.ligne and Coup.colonne == coup.colonne):
			return True
	return False

def joueCoup(jeu,coup):
	"""jeu*coup->void
		Joue un coup a l'aide de la fonction joueCoup defini dans le module game
		Hypothese:le coup est valide
 		Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
	"""
	game.updatePlateauScore(jeu, coup)
	jeu.coups_joues.append(coup)
	jeu.coups_possibles = [None]
	changeJoueur(jeu)
	
	

def initialiseJeu():
	""" void -> jeu
		Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
	"""
	jeu = Jeu(game.lignes, game.colonnes, [], [None], 1, [0, 0])
	game.initialiseJeu(jeu)
	return jeu

def getGagnant(jeu):
	"""jeu->nat
		Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
	"""
	score = getScores(jeu)
	res = score[0]-score[1]
	if (res==0):
		return 0
	if (res < 0):
		return 2
	if (res > 0):
		return 1

def afficheCoup(coup):
	""" coup->void
		Affiche un coup
	"""
	print ("ligne:",coup.ligne,"colonne:",coup.colonne)

def affiche(jeu):
	""" jeu->void
		Affiche l'etat du jeu de la maniere suivante :
				Coup joue = <dernier coup>
				Scores = <score 1>, <score 2>
				Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
				Joueur <joueur>, a vous de jouer
				
			Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
	"""
	if (len(getCoupsJoues(jeu)) == 0):
		print ("Premier tour !!!\n")
	else:
		print ("Dernier coup joue = ", end="")
		afficheCoup(getCoupsJoues(jeu)[len(getCoupsJoues(jeu))-1])
	print ("Score = ", getScores(jeu))
	print ("Plateau :")
	print ("   ", end='')
	for i in range(game.colonnes):
		print ("| ", i, " ", end='')
	print ("|")
	for i in range(game.colonnes*6+4):
		print ("-", end='')
	print("")
	for l in range(game.lignes):
		print ("", l, "",end='')
		for c in range(game.colonnes):
			print ("| ", str(getCaseVal(jeu, l, c)), " ", end='')
		print("|")
		for i in range(game.colonnes*6+4):
			print ("-", end='')
		print("")
	print ("Joueur", getJoueur(jeu),", a vous de jouer")


# Fonctions utiles

def getPlateau(jeu):
	""" jeu  -> plateau
		Retourne le plateau du jeu passe en parametre
	"""
	return jeu.plat

def getCoupsJoues(jeu):
	""" jeu  -> List[coup]
		Retourne la liste des coups joues dans le jeu passe en parametre
	"""
	return jeu.coups_joues



def getScores(jeu):
	""" jeu  -> Pair[nat nat]
		Retourne les scores du jeu passe en parametre
	"""
	return jeu.scores

def getJoueur(jeu):
	""" jeu  -> nat
		Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
	"""
	return jeu.joueur

def getLautreJoueur(jeu):
	""" jeu  -> nat
		Retourne le joueur a qui ce n'est pas le tour de jouer dans le jeu passe en parametre
	"""
	if (jeu.joueur == 1):
		return 2
	return 1

def changeJoueur(jeu):
	""" jeu  -> void
		Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
	"""
	Joueur = getJoueur(jeu)
	if (Joueur == 1):
		jeu.joueur = 2
	else:
		jeu.joueur = 1

def getScore(jeu,joueur):
	""" jeu*nat->int
		Retourne le score du joueur
		Hypothese: le joueur est 1 ou 2
	"""
	return getScores(jeu)[joueur-1]

def getCaseVal(jeu, ligne, colonne):
	""" jeu*nat*nat -> nat
		Retourne le contenu de la case ligne,colonne du jeu
		Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
	"""
	return jeu.plat.plateau[ligne][colonne]
    
    




