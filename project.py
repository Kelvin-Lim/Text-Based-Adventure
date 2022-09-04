#Text Based Adventure Project
#
#Classes:
from random import randint

class Equipment():
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp

class Player():
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.defending = False
        self.items = []
        self.alive = True
    
    def attack_target(self, enemy):
        self.defending = False
        if self.attack > enemy.defense:
            enemy.hp = enemy.hp - (self.attack - enemy.defense)

    def defend_self(self):
        self.defending = True

    def check_status(self):
        print("Your name is {name}. You have {hp} hp, {attack} attack, and {defense} defense.".format(name = self.name, hp = self.hp, attack = self.attack, defense = self.defense))
        print("The items you're holding are:")
        print(self.items)

    def pickup_equipment(self, equip):
        self.attack += equip.attack
        self.defense += equip.defense
        self.hp += equip.hp
        self.items.append(equip.name)

class Monster():
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.alive = True
    
    def attack_target(self, player):
        if player.defending == True:
            if self.attack > player.defense * 2:
                player.hp = player.hp - (self.attack - player.defense * 2)
        else:
            if self.attack > player.defense:
                player.hp = player.hp - (self.attack - player.defense)

#Creating equipment, monsters, player
sword = Equipment("Sword", 5, 0, 0)
shield = Equipment("Shield", 0, 5, 2)
armor = Equipment("Armor", 0, 3, 8)
magic_armor = Equipment("Magic Armor", 2, 5, 12)
magic_sword = Equipment("Magic Sword", 10, 0, 2)
magic_shield = Equipment("Magic Shield", 0, 10, 3)

slime = Monster("Slime", 2, 3, 10)
goblin = Monster("Goblin", 3, 1, 8)
orc = Monster("Orc", 7, 5, 18)
dragon = Monster("Dragon",20, 10, 50)


#Story Functions:
#Intro and first choice:
def intro():
    print("This is a magical world that you've woken up in.")
    player_name = input("You remember that your name is... ")
    print("You've woken in an empty field under a tree. You can see a village nearby, some mountains, and a forest.")
    return player_name

#tutorial_sign_count = 0
def tutorial_sign():
    print("At any point where you can make a choice, you can look at your player stats by typing: Stats.")
    print("Sometimes, there may be hidden choices as well...")
    print()
    print("That sign made no sense to you. Who wrote that?")
    #if tutorial_sign_count > 0:
        #print("Wait... Haven't you seen that sign before?")
    print()
    #tutorial_sign_count += 1
    #return tutorial_sign_count

def tree_search():
    print("You decide to search the tree.")
    print("You walk around to the back of the tree and find a chest. Upon opening it, you find a sword.")
    player.pickup_equipment(sword)

def village():
    print("You decide to head to the village.")
    print("On the way there, you see a sign.")
    tutorial_sign()
    print("When you reach the village, you can hear a commotion coming from the town square.")
    print("You walk over and see a large gathering of people around a man standing on a box.")
    print("The man is holding up a sign with stick figures drawn on it. You can't really tell what they are supposed to be.")
    print()
    print("The man sees you and yells: \"As foretold in the sacred texts! The hero has come to save us all from the dragon!\"")
    print("He runs over to you and points to one of the stick figures. \"See? Wait hold on...\" He takes out a pencil and edits the stick figure a bit.")
    print("\"You have been sent by the heavens above to kill the dragon and end the terror. You\'ll do it right?\" Everyone is watching you expectantly.")
    print()


def mountains():
    print("You decide to head to the mountains.")
    print("On the way there, you see a sign.")
    tutorial_sign()
    print("Continuing on, you see a group of knights on horses. They stop to speak with you as they draw near.")
    print("\"Stop! Are you headed to the mountains? With nothing to protect you? Here take this. It belonged to our trainee... and he is no longer with us.\"")
    print("The knight hands you a shield. \"He fell in battle with the dragon that resides on that mountain. You really shouldn't go though.\"")
    player.pickup_equipment(shield)
    print("\"Come back to the village with us. It's safer. Plus you look like you could use a meal.\"")
    print()
    

def forest():
    print("You decide to head to the forest.")
    print("On the way there, you see a sign.")
    tutorial_sign()
    print("Suddenly, you fall into a pit trap and die.")
    print("GAME OVER.")
    print()

def nap():
    print("You decide to take a nap.")
    print("While you are napping, an apple falls on your head.")
    print("Unfortunately, this apple was enchanted with gravitational magic and the weight of it crushed you, killing you instantly.")
    print("GAME OVER.")
    print()

#Second choice story functions:
def mountain_bad():
    print("You decided to ignore the nice knight's warning and continue onward to the mountain.")
    print("By the time you reach the mountain, the sun is beginning to set so you decide to make camp.")
    print("Or you would... if you had any supplies. You found some branches to start a fire with.")
    print("As you are setting up your makeshift camp, you hear a loud roar and then some rumbling.")
    print("You look around for the source of the sound and turn to see a giant boulder rolling down the mountain, quickly crushing you.")
    print("GAME OVER.")
    print()

def prophecy_choice_yes():
    print("You accept the quest. The townspeople cheer and the man looks at you.")
    print("He says \"You don't look very heroic though... Ah I know! Have this armor that I definitely acquired legally just for you!\"")
    player.pickup_equipment(armor)
    print("\"Now go! To the mountain\" He rushes you out of the village before you can protest.")
    print()

def prophecy_choice_no():
    print("The man stares at you for a bit. He looks back at his drawing, crosses out the stick figure he edited before, and draws on the other one.")
    print("He says \"Ah... It appears I was wrong. The sacred texts actually say that you are the villian that will plunge this land into darkness... Guards!\"")
    print("You are quickly swarmed by the village guards who lock you up with no trial to defend yourself.")
    print("GAME OVER.")
    print()

#Final story functions
def mountain_boss_fight(player, boss):
    print("You rush to the mountain. On your way there, you see a large dragon flying around the mountain. It spots you and lands in front of you.")
    while boss.alive and player.alive == True:
        player_choice_check = 0
        while player_choice_check == 0:
            player_action = input("What will you do? You can attack or defend. Please type A or D.")
            if player_action.upper() == "A":
                player.attack_target(boss)
                print("You deal " + str((player.attack - boss.defense)) + " damage!")
                player_choice_check = 1
                if boss.hp <= 0:
                    print("You have slain the dragon! Congratulations!")
                    print("GAME OVER.")
                    boss.alive = False
            elif player_action.upper() == "D":
                player.defend_self()
                print("You are now defending!")
                player_choice_check = 1
            elif player_action.upper() == "STATS":
                player.check_status()
            else:
                print("Please pick one of the given choices.")
        boss.attack_target(player)
        #SHOULD ADD LINE THAT SAYS HOW MUCH DMG DRAGON DOES AND CURRENT HP
        if player.hp <= 0:
            print("You have died.")
            print("GAME OVER.")
            player.alive = False
        


#Game Start:
player_name = intro()
player = Player(player_name, randint(10, 20), randint(10, 20), randint(10, 25))
print()
loop_check = 0
village_route = False
forest_route = False
tree_check = 0
while loop_check == 0:
    first_choice = input("What would you like to do? You can search the tree, head to the village, head to the mountains, head to the forest, or take a nap. Please type T, V, M, F, or N. ")
    print()
    if first_choice.upper() == "T":
        if tree_check == 0:
            tree_search()
            tree_check = 1
        elif tree_check == 1:
            print("You already searched the tree.")
    elif first_choice.upper() == "V":
        village()
        loop_check = 1
        village_route = True
    elif first_choice.upper() == "M":
        mountains()
        loop_check = 1
        loop_check2 = 0
        while loop_check2 == 0:
            mountain_choice = input("Will you heed the knight's words and go to the village? Or will you continue to the mountain? Please type V or M.")
            print()
            if mountain_choice.upper() == "V":
                village()
                village_route = True
                loop_check2 = 1
            elif mountain_choice.upper() == "M":
                mountain_bad()
                loop_check2 = 1
            elif mountain_choice.upper() == "STATS":
                player.check_status()
            print()
    elif first_choice.upper() == "F":
        forest()
        loop_check = 1
        forest_route = True
    elif first_choice.upper() == "N":
        nap()
        loop_check = 1
    else:
        print("Please pick one of the letters corresponding with the choices. T = Tree, V = Village, M = Mountains, F = Forest, N = Nap ")

#Second major choice
if village_route == True:
    village_loop_check = 0
    while village_loop_check == 0:
        prophecy_check = input("Will you accept the quest? Please type Y or N.")
        print()
        if prophecy_check.upper() == "Y":
            prophecy_choice_yes()
            village_loop_check = 1
        elif prophecy_check.upper() == "N":
            prophecy_choice_no()
            village_loop_check = 2
        elif prophecy_check.upper() == "STATS":
            player.check_status()
            print()
    if village_loop_check == 1:
        mountain_boss_fight(player, dragon)
elif forest_route == True:
    pass