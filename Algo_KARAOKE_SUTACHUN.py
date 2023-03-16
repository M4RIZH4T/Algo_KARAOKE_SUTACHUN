#Test POO 16/03/2023 

#--------------------------------- SCORES DE KARAOKE : Exercice A ---------------------------------

#1 & 2 : modéliser la classe Player et écrire le constructeur de la classe. -----------------------

class Player : 
    def __init__ (self, pseudo, scoreTotal, scoreChanson1, scoreChanson2, scoreChanson3, scoreChanson4, scoreChanson5) : 
        
        self.__name = pseudo 
        self.__score = scoreTotal 
        self.__score0 = scoreChanson1
        self.__score1 = scoreChanson2
        self.__score2 = scoreChanson3 
        self.__score3 = scoreChanson4 
        self.__score4 = scoreChanson5
     

#3 : implémenter les méthodes de la classe. ------------------------------------------------------- 

    def getPseudo (self) : 

        print ("Pseudo : " + self.__name)

    def getScoreTotal (self) : 

        total = str(self.__score0 + self.__score1 + self.__score2 + self.__score3 + self.__score4)
        self.__score = total 
        print ("Le score total de " + self.__name + " est : " + self.__score )

    #problème avec la division  
    def getMoyenneScore (self) :

        total = str(self.__score)   
        moyenne = (total // 5) 
        print ("Le score moyen de " + self.__name + " est : " + moyenne )

    def ajoutScore (self) : 

        numero = input("Quel est le numéro de chanson ?") 

        #chanson1
        if (numero == "0") : 
            scoreObtenu = input("Quel score avez vous obtenu ?")
            if (self.__score0 < scoreObtenu) : 
                self.__score0 = scoreObtenu 
                print ("Vous avez ajouté un score de : " + self.__score0 + " pour la chanson " + numero )
            else : 
                print ("Votre score reste le même : " + self.__score0)
        else : 
            print ("Numéro de chanson non valide.")

        #chanson2
        if (numero == "1") : 
            scoreObtenu = input("Quel score avez vous obtenu ?")
            if (self.__score1 < scoreObtenu) : 
                self.__score1 = scoreObtenu 
                print ("Vous avez ajouté un score de : " + self.__score1 + " pour la chanson " + numero )
            else : 
                print ("Votre score reste le même : " + self.__score1)
        else : 
            print ("Numéro de chanson non valide.")

        #chanson3
        if (numero == "2") : 
            scoreObtenu = input("Quel score avez vous obtenu ?")
            if (self.__score2 < scoreObtenu) : 
                self.__score2 = scoreObtenu 
                print ("Vous avez ajouté un score de : " + self.__score2 + " pour la chanson " + numero )
            else : 
                print ("Votre score reste le même : " + self.__score2)
        else : 
            print ("Numéro de chanson non valide.")

        #chanson4
        if (numero == "3") : 
            scoreObtenu = input("Quel score avez vous obtenu ?")
            if (self.__score3 < scoreObtenu) : 
                self.__score3 = scoreObtenu 
                print ("Vous avez ajouté un score de : " + self.__score3 + " pour la chanson " + numero )
            else : 
                print ("Votre score reste le même : " + self.__score3)
        else : 
            print ("Numéro de chanson non valide.")

        #chanson5
        if (numero == "4") : 
            scoreObtenu = input("Quel score avez vous obtenu ?")
            if (self.__score4 < scoreObtenu) : 
                self.__score4 = scoreObtenu 
                print ("Vous avez ajouté un score de : " + self.__score4 + " pour la chanson " + numero )
            else : 
                print ("Votre score reste le même : " + self.__score4)
        else : 
            print ("Numéro de chanson non valide.")

    def getScore (self) : 

        numero = input ("Pour quel numéro de chanson souhaiteriez-vous connaître le score ? ")

        #chanson1
        if (numero == "0") : 
            print ("Votre score pour la chanson 1 est de : " + self.__score0)
        else : 
            print ("Numéro de chanson non valide.")

        #chanson2
        if (numero == "1") : 
            print ("Votre score pour la chanson 2 est de : " + self.__score1)
        else : 
            print ("Numéro de chanson non valide.")
        
        #chanson3
        if (numero == "2") : 
            print ("Votre score pour la chanson 3 est de : " + self.__score2)
        else : 
            print ("Numéro de chanson non valide.")

        #chanson4
        if (numero == "3") : 
            print ("Votre score pour la chanson 4 est de : " + self.__score3)
        else : 
            print ("Numéro de chanson non valide.")

        #chanson5
        if (numero == "4") : 
            print ("Votre score pour la chanson 5 est de : " + self.__score4)
        else : 
            print ("Numéro de chanson non valide.")


scoreMin = 50 
scoreMax = 100 

#4 : vérifier la pertinance de l'implémentation. --------------------------------------------------
#test 
Patrick = Player("Patrick", 0, 50, 50, 50, 50, 50)

Patrick.getPseudo() 
Patrick.getScoreTotal() 
Patrick.getMoyenneScore() #marche pas 


#--------------------------------- SCORES DE KARAOKE : Exercice B ---------------------------------

#1 & 2 : modéliser, déclarer et implémenter la classe Karaoke et modifier la classe Player --------

class Karaoke : 

    def __init__ (self, nombreChansons, nomChanson, nombrePlayers, meilleurScoreChanson) : 
        self.__numberSongs = nombreChansons 
        self.__nameSong = nomChanson 
        self.__numberPlayers = nombrePlayers 
        self.__bestScoreSong = meilleurScoreChanson 

    def ajoutPlayer (self) : 

        ajout = input ("Combien de joueurs souhaitez vous ajouter ? ") 
        self.__numberPlayers += ajout 
        print ("Vous avez ajouté " + ajout + "Players. Vous êtes maintenant " + self.__numberPlayers)

    def suppressionPlayer (self) : 

        suppression = input ("Combien de joueurs souhaitez vous enlever ?") 
        self.__numberPlayers -= suppression
        if (self.__numberPlayers < 1) : 
            print ("Vous ne pouvez pas supprimer de players car il n'en restera plus.")
        else : 
            print ("Vous avez supprimé " + suppression + "Players. Vous êtes maintenant " + self.__numberPlayers)
        
class Player : 

    def __init__ (self, meilleurScoreTotal, meilleurScoreToutesChansons, meilleureMoyenne) :
        self.__bestScoreTotal = meilleurScoreTotal 
        self.__bestScoreAllSongs = meilleurScoreToutesChansons 
        self.__bestAverageScore = meilleureMoyenne

    def recordScoreTotal (self) : 
        print ("Le meilleur score total est de : " + self.__bestScoreTotal + "points.")

    def recordScoreToutesChansons (self) : 
        print ("Le meilleur score toutes chansons confondues est de : " + self.__bestScoreAllSongs + "points.")

    def recordMeilleureMoyenne (self) : 
        print ("La meilleure moyenne est de : " + self.__bestAverageScore + "points.")


#3 : tester ---------------------------------------------------------------------------------------

