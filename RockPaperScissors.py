# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:47:08 2021

@author: Naim
"""

print("JEU PIERRE FEUILLE CISEAU ....  BONNE CHANCE !!")

print("---------------------------------------------------")
import random

nom = input("Veuillez saisir votre nom : ")
user_victoires = 0
pc_victoires = 0
nuls = 0

while True:
    print(nom, " : ", user_victoires, " égalité : ", nuls, " PC : ", pc_victoires)
    coupJoueur = input("Entrez votre coup: (p)ierre, (f)euille, (c)iseaux ou (q)uitter :")
    if coupJoueur == "q":
        print("Vous avez quittez...")
        break
    if coupJoueur != "p" and coupJoueur != "f" and coupJoueur != "c":
        continue

    if coupJoueur == "p":
        print("PIERRE contre ...", end=" ")
    elif coupJoueur == "f":
        print("Feuille contre ...", end=" ")
    else:
        print("CISEAUX contre ...", end=" ")

    randomNombre = random.randint(1, 3)
    if randomNombre == 1:
        coupPC = "p"
        print("PIERRE")
    elif randomNombre == 2:
        coupPC = "f"
        print("FEUILLE")
    else:
        coupPC = "c"
        print("CISEAUX")

    if coupJoueur == coupPC:
        print("Partie est nulle !")
        nuls = nuls + 1
    elif coupJoueur == "p" and coupPC == "c":
        print("Vous avez gagnée ! ")
        user_victoires = user_victoires + 1
    elif coupJoueur == "f" and coupPC == "p":
        print("Vous avez gagnée !")
        user_victoires = user_victoires + 1
    elif coupJoueur == "c" and coupPC == "f":
        print("Vous avez gagnée ! ")
        user_victoires = user_victoires + 1
    elif coupJoueur == "p" and coupPC == "f":
        print("Vous avez perdu !")
        pc_victoires = pc_victoires + 1
    elif coupJoueur == "f" and coupPC == "c":
        print("Vous avez perdu !")
        pc_victoires = pc_victoires + 1
    elif coupJoueur == "c" and coupPC == "p":
        print("Vous avez perdu!")
        pc_victoires = pc_victoires + 1






