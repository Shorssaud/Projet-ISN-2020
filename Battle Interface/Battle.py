from Player import *
from Ennemy import *
from random import *
from operator import *

# Crée une classe 'Battle()'
class Battle:

    # Fonction lancée en tout premier lorsqu'on fait appel à la classe 'Battle()'
    def __init__(self, mobName1, mobName2=None, mobName3=None):

        self.mobName1=mobName1
        self.mobName2=mobName2
        self.mobName3=mobName3

        # fait appel à la fonction 'BattleSettings'
        self.BattleSettings(mobName1, mobName2, mobName3)

        # fait tourner tout le programme
        self.loop = 1
        while self.loop == 1:

            # fait appel à la fonction 'DeathVerifier()'
            self.DeathVerifier()

            # fait appel à la fonction 'WinLose()'
            self.WinLose()

 

            # prévention pour ne pas faire appel à la fonction 'Action()' alors que 'self.loop' == 0
            if self.loop == 1:
                self.Action()


    # Réglages avant que le combat commence
    def BattleSettings(self, mobName1, mobName2, mobName3):
    
        # crée une liste vide 'actionOrderArray'
        self.actionOrderSettingArray = []

        # recrée une variable pour chaque stat du Player
        self.pName = Player.Name
        self.pHP = Player.HP
        self.pMP = Player.MP
        self.pAtk = Player.Atk
        self.pDef = Player.Def
        self.pSpeed = Player.Speed

        #ajoute ["p", vitesse du Player] dans 'actionOrderSettingArray' pour être présent dans le combat
        self.actionOrderSettingArray.append(["p", self.pSpeed])

        self.m1Name = mobName1.Name
        self.m1HP = mobName1.HP
        self.m1MP = mobName1.MP
        self.m1Atk = mobName1.Atk
        self.m1Def = mobName1.Def
        self.m1Speed = mobName1.Speed

        self.mobAmount = 1

        self.actionOrderSettingArray.append(["m1", self.m1Speed])

        if mobName2 != None:
            self.m2Name = mobName2.Name
            self.m2HP = mobName2.HP
            self.m2MP = mobName2.MP
            self.m2Atk = mobName2.Atk
            self.m2Def = mobName2.Def
            self.m2Speed = mobName2.Speed

            self.mobAmount = 2
            
            self.actionOrderSettingArray.append(["m2", self.m2Speed])

            if mobName3 != None:
                self.m3Name = mobName3.Name
                self.m3HP = mobName3.HP
                self.m3MP = mobName3.MP
                self.m3Atk = mobName3.Atk
                self.m3Def = mobName3.Def
                self.m3Speed = mobName3.Speed

                self.mobAmount = 3

                self.actionOrderSettingArray.append(["m3", self.m3Speed])



    # Définit l'odre dans lequel les combattants vont jouer
    def ActionOrder(self):

        self.actionOrderArray=[]

        # reclasse les listes de 'actionOrderSettingArray' selon leur 2ème valeur, dans l'ordre décroissant
        self.actionOrderSettingArray.sort(key=itemgetter(1), reverse=True)

        # crée une liste 'actionOrderArray' dans laquelle il y aura le nom des combattants classé selon leur vitesse, et la return
        for i in range(len(self.actionOrderSettingArray)):
            self.actionOrderArray.append(self.actionOrderSettingArray[i][0])
        return self.actionOrderArray
        


    # Déninit l'action que va faire le Player
    def PlayerActionSelection(self):

        # demande au Player de choisir une action
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.SkipLine(2)
        self.ShowFightersHP()
        self.SkipLine(4)
        self.actionSelection = int(input("Action Selection  |  1 : Attack  |  2 : Guard  |  3 : Use item  |  4 : Flee  |  : "))
            
        # si le Player choisi d'Attack :
        if self.actionSelection == 1:
            self.SkipLine(2)

            # s'il y a 3 mobs en vie :
            if self.mobAmount == 3:

                self.defender = int(input("Attack  |  1 : " + self.m1Name + "  |  2 : " + self.m2Name + "  |  3 : " + self.m3Name + "  |  4 : Cancel  |  : "))
                if self.defender == 4:
                    self.defender = "cancel"

            # s'il y a 2 mobs en vie :
            elif self.mobAmount == 2:

                # si Mob3  existe et Mob2 est mort :
                if self.mobName3 != None and self.m2HP == "DEAD":
                    self.defender = int(input("Attack  |  1 : " + self.m1Name + "  |  2 : " + self.m3Name + "  |  3 : Cancel  |  : "))
                    if self.defender == 3:
                        self.defender = "cancel"
                    elif self.defender == 2:
                        self.defender = 3
                        
                elif self.mobName3 != None and self.m1HP == "DEAD":
                    self.defender = int(input("Attack  |  1 : " + self.m2Name + "  |  2 : " + self.m3Name + "  |  3 : Cancel  |  : "))
                    if self.defender == 3:
                        self.defender = "cancel"
                    else:
                        self.defender = self.defender + 1
                        
                else:
                    self.defender = int(input("Attack  |  1 : " + self.m1Name + "  |  2 : " + self.m2Name + "  |  3 : Cancel  |  : "))
                    if self.defender == 3:
                        self.defender = "cancel"

            elif self.mobAmount == 1:

                if self.mobName2 != None and self.m1HP == "DEAD" and self.m2HP == "DEAD":
                    self.defender = int(input("Attack  |  1 : " + self.m3Name + "  |  2 : Cancel  |  : "))
                    if self.defender == 2:
                        self.defender = "cancel"
                    else:
                        self.defender = 3

                elif self.mobName2 != None and self.m1HP == "DEAD" and self.m3HP == "DEAD":
                    self.defender = int(input("Attack  |  1 : " + self.m2Name + "  |  2 : Cancel  |  : "))
                    if self.defender == 2:
                        self.defender = "cancel"
                    else:
                        self.defender = 2
                else: 
                    self.defender = int(input("Attack  |  1 : " + self.m1Name + "  |  2 : Cancel  |  : "))
                    if self.defender == 2:
                        self.defender = "cancel"

            # si le Player n'a pas choisi de Cancel, return "Attack"
            if self.defender != "cancel":
                if self.defender == 1 or self.defender == 2 or self.defender == 3:
                    return "Attack"

        # si le Player a choisi de Guard :
        elif self.actionSelection == 2:
            self.SkipLine(2)
            self.ask = int(input("Guard  |  1 : Accept  |  2 : Cancel  |  : "))

            # s'il accepte, return "Guard"
            if self.ask == 1:
                return "Guard"

        #si le Player a choisi de Use item :
        elif self.actionSelection == 3:
            return None

        #si le Player a choisi de Flee :
        elif self.actionSelection == 4:
            self.SkipLine(2)
            self.ask = int(input("Flee  |  1 : Accept  |  2 : Cancel  |  : "))

            #s'il accepte, return "Flee"
            if self.ask == 1:
                return "Flee"


    # Déninit l'action que va faire le Mob
    def MobActionSelection(self):
        self.actionSelection = randint(1,2)
        if self.actionSelection == 1:
            return "Attack"
        elif self.actionSelection == 2:
            return "Guard"
        elif self.actionSelection == 3:
            return "Use item"
        else:
            return "Flee"


    
                    

    # Exécute les actions des combattants
    def Action(self):

        # définit l'odre dans lequel les combattants vont jouer
        self.actionOrderArray = self.ActionOrder()

        
        # réinitialise les variables 'xAction' pour chaque combattant
        self.pAction = None
        self.m1Action = None
        self.m2Action = None
        self.m3Action = None
        
        # déninit l'action que vont faire les combattants
        while self.pAction == None:
            self.pAction = self.PlayerActionSelection()
        if self.m1HP != "DEAD":
            self.m1Action = self.MobActionSelection()
        if self.mobName2 != None and self.m2HP != "DEAD":
            self.m2Action = self.MobActionSelection()
        if self.mobName3 != None and self.m3HP != "DEAD":
            self.m3Action = self.MobActionSelection()

        # si le combattant utilise "Guard", exécuter 'Guard()'

        self.SkipLine(2)
        
        self.pGuard = 0
        self.m1Guard = 0
        self.m2Guard = 0
        self.m3Guard = 0
        if self.pAction == "Guard":
            self.Guard("p")
        if self.m1Action == "Guard":
            self.Guard("m1")
        if self.mobName2 != None:
            if self.m2Action == "Guard":
                self.Guard("m2")
            if self.mobName3 != None:
                if self.m3Action == "Guard":
                    self.Guard("m3")
        
        # répète le nombre de fois qu'il y a de combattants:
        for i in range(len(self.actionOrderArray)):

            # si la i ème valeur est "p", alors:
            if self.actionOrderArray[i] == "p":

                # si "p" a choisi l'action "Attack", exécuter 'Attack()'
                if self.pAction == "Attack":

                    if self.defender == 1:
                        self.defender = "m1"
                    elif self.defender == 2:
                        self.defender = "m2"
                    else:
                        self.defender = "m3"
                        
                    self.Attack("p", self.defender)
                    
                # si "p" a choisi l'action "UseItem", exécuter 'UseItem()'
                if self.pAction == "Use item":
                    None

                # si "p" a choisi l'action "Flee", exécuter 'Flee()'
                if self.pAction == "Flee":
                    self.Flee()
                            
            if self.actionOrderArray[i] == "m1":
                if self.m1Action == "Attack":
                    self.Attack("m1", "p")

            if self.actionOrderArray[i] == "m2":
                if self.m2Action == "Attack":
                    self.Attack("m2", "p")

            if self.actionOrderArray[i] == "m3":
                if self.m3Action == "Attack":
                    self.Attack("m3", "p")

        # Exécute la fonction 'GuardEnd()' 
        self.GuardEnd()

        self.SkipLine(2)
        x=input("-- Appuyez sur 'Entrée' --")
        self.SkipLine(2)

    
            
    # Système d'Attack
    def Attack(self, attacker, defender):

        # si Player attaque et Mob1 défend :
        if attacker == "p" and defender == "m1":

            # si la Def de Mob1 est plus petite ou égale à l'Atk du Player
            if self.m1Def <= self.pAtk:
                print(self.pName + " inflicted", self.pAtk - self.m1Def, "damage to the " + self.m1Name)
                self.m1HP = self.m1HP - self.pAtk + self.m1Def

            # si la Def de Mob1 est est plus grande que l'Atk du Player
            else:
                print(self.pName + " inflicted 0 damage to the " + self.m1Name)
            
        elif attacker == "p" and defender == "m2":
            if self.m2Def <= self.pAtk:
                print(self.pName + " inflicted", self.pAtk - self.m2Def, "damage to the " + self.m2Name)
                self.m2HP = self.m2HP - self.pAtk + self.m2Def
            else:
                print(self.pName + " inflicted 0 damage to the " + self.m2Name)
            
        elif attacker == "p" and defender == "m3":
            if self.m3Def <= self.pAtk:
                print(self.pName + " inflicted", self.pAtk - self.m3Def, "damage to the " + self.m3Name)
                self.m3HP = self.m3HP - self.pAtk + self.m3Def
            else:
                print(self.pName + " inflicted 0 damage to the " + self.m3Name)
   

        elif attacker == "m1" and defender == "p":
            if self.pDef <= self.m1Atk:
                print(self.m1Name + " inflicted", self.m1Atk - self.pDef, "damage to " + self.pName)
                self.pHP = self.pHP - self.m1Atk + self.pDef
            else:
                print(self.m1Name + " inflicted 0 damage to " + self.pName)

        elif attacker == "m2" and defender == "p":
            if self.pDef <= self.m2Atk:
                print(self.m2Name + " inflicted", self.m2Atk - self.pDef, "damage to " + self.pName)
                self.pHP = self.pHP - self.m2Atk + self.pDef
            else:
                print(self.m2Name + " inflicted 0 damage to " + self.pName)

        elif attacker == "m3" and defender == "p":
            if self.pDef <= self.m3Atk:
                print(self.m3Name + " inflicted", self.m3Atk - self.pDef, "damage to " + self.pName)
                self.pHP = self.pHP - self.m3Atk + self.pDef
            else:
                print(self.m3Name + " inflicted 0 damage to " + self.pName)
        

    #Système de Guard
    def Guard(self, guardian):
        if guardian == "p":
            print(self.pName + " blocked")
            self.pDef = self.pDef * 2
            self.pGuard = 1
        if guardian == "m1":
            print(self.m1Name + " blocked")
            self.m1Def = self.m1Def * 2
            self.m1Guard = 1
        if guardian == "m2":
            print(self.m2Name + " blocked")
            self.m2Def = self.m2Def * 2
            self.m2Guard = 1
        if guardian == "m3":
            print(self.m3Name + " blocked")
            self.m3Def = self.m3Def * 2
            self.m3Guard = 1

    # Fin du Guard
    def GuardEnd(self):
        if self.pGuard == 1:
            self.pDef = self.pDef / 2
            self.pGuard = 0
        if self.m1Guard == 1:
            self.m1Def = self.m1Def / 2
            self.m1Guard = 0
        if self.m2Guard == 1:
            self.m2Def = self.m2Def / 2
            self.m2Guard = 0
        if self.m3Guard == 1:
            self.m3Def = self.m3Def / 2
            self.m3Guard = 0

    # Système de Flee
    def Flee(self):
        
        fleeProbability = randint(1,10)

        # 80% de chance de succès
        if fleeProbability <= 7:
            print("flee succeed")
            self.loop = 0

        # 20% de chance d'échec
        else:
            print("flee failed")

    # Afficher les HP de tous les combattants
    def ShowFightersHP(self):

        print(self.pName + "  |  HP :", self.pHP)

        self.SkipLine(5)

        print(self.m1Name + "  |  HP :", self.m1HP)

            
        if self.mobName2 != None:
            self.SkipLine(2)
            print(self.m2Name + "  |  HP :", self.m2HP)
            
            if self.mobName3 != None:
                self.SkipLine(2)
                print(self.m3Name + "  |  HP :", self.m3HP)


    # Vérifie si un combattant est mort ou pas
    def DeathVerifier(self):
        if self.pHP != "DEAD" and self.pHP <= 0:
            self.pHP = "DEAD"
            
        elif self.m1HP != "DEAD" and self.m1HP <= 0:
            self.m1HP = "DEAD"
            self.mobAmount = self.mobAmount - 1
        
        elif self.mobName2 != None and self.m2HP != "DEAD" and self.m2HP <= 0:
            self.m2HP = "DEAD"
            self.mobAmount = self.mobAmount - 1
            
        elif self.mobName3 != None and self.m3HP != "DEAD" and self.m3HP <= 0:
            self.m3HP = "DEAD"
            self.mobAmount = self.mobAmount - 1
            
        else :
            return False
    
    # Reconnait si on a gagné / perdu / fait une égalité
    def WinLose(self):
        if self.pHP == "DEAD" and self.mobAmount == 0:
            print()
            print("Draw")
            self.loop = 0
        elif self.mobAmount == 0:
            print()
            print(self.pName + " won the battle")
            self.loop = 0
        elif self.pHP == "DEAD":
            print()
            print(self.pName + " lost the battle")
            self.loop = 0


    # Saute des lignes
    def SkipLine(self, line):
        for i in range(line):
            print()


