#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:01:55 2019

@author: val
"""

class Resistant:
    __pseudo = None
    __lesMessages = None
    __flotteAlliee = None
    
    def __init__(self,pseudo,lesMessages,flotteAlliee):
        self.__pseudo = pseudo
        self.__flotteAlliee = flotteAlliee
        self.__lesMessages = lesMessages
        
    def getMessages(self):
        return self.__lesMessages
    
    def getPseudo(self):
        return self.__pseudo
        
    
class FlotteAlliee:
    __pseudo = None
    
    def __init__(self,pseudo):
        self.__pseudo = pseudo
    
class SaboteurFerroviaire:
    __pseudo = None
    
    def __init__(self,pseudo):
        self.__pseudo = pseudo
        
    def getPseudo(self,pseudo):
        self.__pseudo = pseudo
        print("")

class RadioLondres:
    __leResistant = None
    __lesMessages = []
    __cptMsg = 0
    __nbMsg = 0
    leMessageLu = ""
    __observer = []
    
    def __init__(self,resistant):
        self.__leResistant = resistant
        self.__lesMessages = resistant.getMessages()
        self.__nbMsg = len(self.__lesMessages)
        
    def diffuseMessage(self):
            self.leMessageLu = self.__lesMessages[self.__cptMsg]
            self.setChanged()
            print("Message diffusé " + self.leMessageLu + "\n")
            return self.leMessageLu
        
    def getResistant(self,leResistant):
        return self.__leResistant
        
    def arretEcoute(self):
        print("Arret de la diffusion")
        
    def setChanged(self):
        for observer in self.__observer:
            observer.update()
        
    def addObserver(self,observer):
        self.__observer.append(observer)
    
    def RadioOn(self):
        while self.__cptMsg < self.__nbMsg:
            self.diffuseMessage()
            self.__cptMsg += 1
        else :
            self.arretEcoute()

        
    
class Envahisseur:
    __pseudo = ""
    __radioLondres = None
    __leMessageEntendu =""
    
    def __init__(self,pseudo, Radio):
        self.__pseudo = pseudo
        self.__radioLondres = Radio
    
    def jecoute(self):
        self.__leMessageEntendu = self.__radioLondres.leMessageLu
        print("Les allemands ont entendu " + self.__leMessageEntendu)
    
    def update(self):
        self.jecoute()
    
    def run(self):
        print("Nous sommes les " + self.__pseudo)
    
    
class GroupeClandestin:
    __pseudo = None
    __radioLondres = None
    __saboteurs = None
    __arretEcoute = True
    __debarquement = False
    __lesMessages = None
    __leMessageEntendu = ""
    __leMessageAttendu = "Les sanglots long des violons de l automne"
    
    def __init__(self,pseudo,radioLondres,saboteur,leMessageAttendu):
        self.__radioLondres = radioLondres
        self.__pseudo = pseudo
        
    def jecoute(self):
        self.__leMessageEntendu = self.__radioLondres.leMessageLu
        print("Le groupe " + self.__pseudo + " a bien entendu le message " + self.__leMessageEntendu)
        if self.__leMessageEntendu == self.__leMessageAttendu:
            self.__arretEcoute = False
            self.__debarquement = True
            
    
    def update(self):
        if self.__arretEcoute == True:
            self.jecoute()
        if self.__debarquement == True:
            print("On debarque")
        else:
            print("En attente du signal")
    
    def run(self):
        if self.__debarquement == True:
            print("On debarque")
        else:
            print("En attente du signal")


#------------------------Programme principale---------------------------------
#Les messages qu'on émets
MessagesRadio = ["Hello","How are you","Fine and you","It s snowing today","Les sanglots long des violons de l automne"]

#Notre flotte alliée
LesAlliees = FlotteAlliee("LesAnglais")

#Notre Résistant (son nom, les messages à diffuser, ses alliées)
DeGaulle = Resistant ("DeGaulle",MessagesRadio,LesAlliees)

#DeGaulle émet à la radio
Radio = RadioLondres(DeGaulle)

#Les envahisseurs nous espionnent
Allemands = Envahisseur("Allemands",Radio)

#Nos saboteurs se préparent
Saboteurs = SaboteurFerroviaire("Vomecourt")

#Groupe Clandestin
Ventriloquist = GroupeClandestin("Ventriloquist",Radio,Saboteurs,"Les sanglots long des violonts de l automne")

#On ajoute les Observeurs
Radio.addObserver(Allemands)
Radio.addObserver(Ventriloquist)

#La radio diffuse
Radio.RadioOn()

#Résultat après avoir écouté
#Ventriloquist.run()
#Allemands.run()