# -*utf-8*
import random
import os
import pickle
#import Données



def liste_random():

    """ affiche la taille de la liste, ajoute cette taille dans la variable taille en int

    puis fais un mot_random = liste_mots[random.randrange(taille)]"""

    with open("les_mots", "r") as fichier_mots:
        texte = fichier_mots.read()
        liste_mots = texte.split(" ")


    taille = len(liste_mots)
    mot_random = liste_mots[random.randrange(taille)]

    return mot_random




def the_game():
    chance = 9
    trouv = {}
    mot_random = liste_random()
    mot_random = mot_random.lower()
    mot_random = mot_random.strip()
    mot = list()
    deja_taper = list()
    j=0
    z=0
    x=0


    for i in mot_random:
        trouv[j]="*"
        j = j + 1
    for i in mot_random:
        mot.append("*")
        x += 1
    print("Le mot que vous devez découvrir contient {} lettres".format(len(trouv)))


    while chance > 0 and mot_random not in mot:
        taper = input("Taper une lettre : ")

        j = 0
        z = 0
        if taper not in mot_random:
            print("Cette lettre ne figure pas dans le mot caché !")
            if taper in deja_taper:
                print("Vous avez déjà tapé cette lettre")


        for i in mot_random:

            if taper == i:

                try:

                    if i == trouv[j]:

                        if i in deja_taper:

                            print("Vous avez déjà tapé cette lettre")

                        else:
                            trouv[j]=i
                            chance = chance + 1
                            print("Bien joué le mot contient bien la lettre {} ".format(i))
                    else:
                        trouv[j]=i
                        chance = chance + 1
                        print("Bien joué le mot contient bien la lettre {} ".format(i))
                        mot[j]=trouv[j]
                except KeyError:
                    trouv[j]=i
                    chance = chance + 1
                    print("Bien joué le mot contient bien la lettre {}".format(i,))

                try:
                    #mot = trouv[0]+trouv[1]+trouv[2]+trouv[3]+trouv[4]+trouv[5]+trouv[6]
                    while z <= len(trouv):

                        mot[z]=trouv[z]
                        z += 1
                except KeyError:
                    pass

            j = j + 1

        if "*" not in mot:
            mot = "".join(mot)



        sorted(trouv.items(),key=lambda t: [0])
        print(mot)



        chance = chance - 1
        print("Il vous reste {} chances !".format(chance))
        deja_taper.append(taper)
        if chance == 7:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/\n")
            print(" |\n")
            print(" |\n")
            print(" |\n")
            print("_|____________\n")
        if chance == 3:
            print("_____________\n")
            print(" | /       |\n")
            print(" |/        O\n")
            print(" |         |\n")
            print(" |\n")
            print(" |\n")
            print("_|____________\n")

    if mot == mot_random:
        print("BRAVO !!! Vous ne mourrez pas aujourd'hui, vous avez trouvé le mot caché : {} !".format(mot))
    elif chance == 0:
        print("Adieu ! AHAHAHAHAHAHHA")
        print("_____________\n")
        print(" | /       |\n")
        print(" |/        O\n")
        print(" |        -|-\n")
        print(" |         /\\\n")
        print(" |\n")
        print("_|____________\n")
        print("\n You are dead")
        print("\nLe mot était {}".format(mot_random))

    global point
    point = chance * 10


def recup_score():
    #On récupère l'objet "score" de "Donnees.py" et on le met dans score_recup
    with open('Donnees.py', 'rb') as donnees:
        mon_depickler = pickle.Unpickler(donnees)
        score = mon_depickler.load()



    return score


def choix_debut():
    choix = ""
    charge_user = ""
    score = recup_score()
    score_user = 0
    global user



    choix = input("Avez-vous déjà fait une partie ?\n oui/non :")
    if choix[0] == "o" or choix[0] == "O":
        for i in score:
            charge_user = charge_user + i + ", "
        print("Les utilisateurs déja enregistré : {}".format(charge_user))
        user = input("Entrez votre nom d'utilisateur : ")

    elif choix[0] == "n" or choix[0] == "N":
        user = input("Entrez votre nom d'utilisateur : ")







def renvoi_score():


    score = recup_score()
    score_user=point
    score[user]=score_user
    try:
        del score[None]
        del score[""]
    except:
        pass
    with open('Donnees.py', 'wb') as donnees:
        mon_pickler = pickle.Pickler(donnees)
        mon_pickler.dump(score)

    print(score)









