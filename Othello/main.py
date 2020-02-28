#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game
import othello
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

#test
JEU = game.initialiseJeu()
"""JEU.plat.plateau[1][1] = 25
print (game.getCaseVal(JEU, 1, 1))"""
#print (othello.getCoupsValides(JEU.plat))


JEU.plat.plateau[3][1] = 1
othello.updatePlateau(JEU, game.coup(4,2))
game.affiche(JEU)
