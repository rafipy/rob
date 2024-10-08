import random

# Dictionaries regarding the locations.

sectors = {
    "0" : 5,
    "1" : 3,
    "2" : 7,
    "3" : 2,
    "4" : 8,
    "5" : 6,
    "6" : 5,
    "7" : 4,
    "8" : 9,
    "9" : 1
    }

# Lists containing items and encounters.

encounters = ("scrap", "respite", )
encounterText = (
    ["You searched the sector, only to find it infested with floorspawn, you suffer grievous bodily harm.", 
     "You searched the sector, spawn of mutated canyne-like flesh jump you from the veil of shadows. Scratches and bruises surface.",
     "You searched the sector, the rubble bashes the top of your puny skull, damaging your optic sensors.",
     "You searched the sector, you awaken the Nightfallbeast it rips the arms from your fleshy torso, putrid ichor sprays on the floor as you desperately tried to escape."],

    "You searched the sector, amidst the rubble and dirt you find a piece of scrap for your lowly base.",

    ["You searched the sector, and there lay the dead carcasses of people that once roamed the surface. They could be used as fuel.",
     "You searched the sector, there stood scarecrows of skinned and flayed humans, exposed muscle, jittering tongues, charred intestines. You stuffed it into yourself.",
     "You searched the sector, the decayed floorspawn, grotesquely colored in a turqoise hue sticks itself to the buildings like slime. They shall work as a fine adhesive."]
                 )

# Player made in a class to essentially "global" the variables.

class controller():
    def __init__(self):
        self.health = 3 
        self.maxHealth = 3
        self.energy = 4

        self.scrapCount = 0
        self.winScrap = 7

        self.woundCount = 0
        
        # Random Starting Position
        self.currentSector = random.choice(list(sectors.keys()))

        # Danger Calculations
        self.dangerCounter = False
        self.extremeDanger = False
        self.totalDanger = 0

player = controller()

# Functions

# Function for moving sectors, fairly straightforward.
def move_to_sec():
    chosen = input("NOW MOVING TOWARDS: ")
    while True:
        if player.energy > 0:

            if chosen in sectors and chosen != player.currentSector:
                line()
                print("\nTRAVEL SUCCESFUL")
                print("ENTERED SECTOR NO.", "06" + chosen,"\n")
                line()
                player.energy -= 1
                return chosen
            
            elif chosen == player.currentSector:
                line()
                print("\nTRAVEL ABORTED.")
                print("You are currently in this sector.\n")
                line()
                return chosen
        
            else:
                line()
                print("\nINVALID SECTOR\n")
                line()
                print()
                map()
                print("\nAbove is the map of available sectors. Select a number (0-9)")
                print("Energy for movement remaining:", player.energy, "clicks.\n")
                chosen = input("NOW MOVING TOWARDS:")
                print()
                
                
        else:
            line()
            print("\nWARNING! Energy too low! \nUNABLE TO MIGRATE!\n")
            line()
            return player.currentSector
            break

# Prints a line, what am I supposed to say here..?

def line(): 
    print("-----------------------------------------------------------------------------------------------------")

# Prints a map.
def map():
    print("                -                                 		    ")		
    print("                \ \                                		    ")
    print("                /    \                             		    ")
    print("                 \    \                             060 = 0	")
    print("                  \    \                            061 = 1 	")
    print("                    \   /                           062 = 2	")
    print("                     `  \                           063 = 3	")
    print("                      |  \                          064 = 4	")
    print("                      | 1 \                         		    ")
    print("                      |     \  ||                   		    ")
    print("                      |      | ||                   		    ")
    print("                      |          \                  065 = 5	")
    print("                     /             \                066 = 6	")
    print("                     |               \    ---\      067 = 7	")
    print("                    /                7 -/     |     068 = 8	")
    print("                   -               8     6   /      069 = 9	")
    print("                 /    9                    /			        ")
    print("             /                           5|			        ")
    print("            |                             |    			    ")
    print("             \ -                     4/ - -    			    ")
    print("                 \                 |           			    ")
    print("                   \                \          			    ")
    print("                    \              3/          			    ")
    print("                     |  2        /             			    ")
    print("                    /          /               			    ")
    print("                   /        /                  			    ")
    print("                   |      /                    			    ")
    print("                   |    /                      			    ")
    print("                   \ 0/						             ")	

# THE ENTIRE GAME IS PLACED IN THIS ONE FUNCTION.
def options():
    print("1 | Travel")
    print("2 | Search")
    print("3 | Inventory")
    print("4 | Status\n")

    print("CURRENTLY SITUATED AT SECTOR", "06" + player.currentSector,"\n")

    # Input has a value error checker to insure that type is indeed an integer.
    retry = True
    while retry:
        try:
            choice = int(input("Select a Choice: "))
            retry = False
        except ValueError:
            retry = True
            print()
            line()
            print("\nIssued command returned as file-type - UNKNOWN. Reissue the command.\n")
            line()

    print()
    
    match choice:
            case 1: # Map and Travel
                
                map()
                line()

                print("\nAbove is the map of available sectors. Select a number (0-9)")
                print("Energy for movement remaining:", player.energy, "clicks.")
                print()
                
                player.currentSector = move_to_sec()
                
            
                player.totalDanger = 0
                print()
                
            # ------------------------------------------------------------------------------------------------------#

            case 2: # Searching and Danger
                search = "yes"
                min = 0
                max = random.randint(2,4)
                player.totalDanger = max * 15
                
                while search != "exit" and player.health > 0:
                    flavorText = random.randint(0, 2)

                    if sectors[player.currentSector] > 0:

                    # ------------------------------------------------------------------------------------------------------#

                    
                        totalDanger = 0
                        
                        rng = random.randint(min,max)
                        

                        if rng == 0:
                            player.totalDanger += 15
                            player.dangerCounter = True
                            situation = encounters[rng]
                        elif rng == 1:
                            player.totalDanger += 15
                            player.dangerCounter = True
                            situation = encounters[rng]
                        else:
                            situation = "attacked"
                            player.totalDanger += 30

                        if player.dangerCounter == True:
                            max += 1
                            player.totalDanger += 15
                            player.dangerCounter = False

                        elif player.extremeDanger == True:
                            player.totalDanger += 30
                            player.extremeDanger = False


                        print("\nYou search the area. CURRENT ABNORMALITY COUNTER: ", player.totalDanger, "%\n", end ="")

                    # ------------------------------------------------------------------------------------------------------#

                        match situation:
                            case "attacked":
                                print(encounterText[0][flavorText])
                                print("\nWARNING! DAMAGE TAKEN!")
                                player.health -= 1
                                print("Remaining damage that can be taken:", player.health,"\n")
                                line()
                                sectors[player.currentSector] -= 1
                                

                            case "scrap":
                                print(encounterText[1])
                                player.scrapCount += 1
                                print("Scrap increased to:", player.scrapCount)
                                print(f"{player.winScrap - player.scrapCount} amounts of scrap remaining.\n")
                                line()
                                sectors[player.currentSector] -= 1
                            
                            case "respite":
                                print(encounterText[2][flavorText])
                                if player.health <= player.maxHealth-1:
                                    player.health += 1
                                else:
                                    player.health = player.maxHealth
                                player.energy += 1
                                print("\nALERT! REPAIRS COMPLETED!")
                                print("Remaining damage that can be taken now increased to:", player.health,"\n")
                                print("Energy restored! Now increased to:", player.energy)
                                line()
                                

                    # ------------------------------------------------------------------------------------------------------#
                    
                    else:
                        print("You searched. There's nothing left here.\n")
                        break
                    
                    print("DETECTING MORE SIGNATURES IN VICINITY. INITIATING CONTINUOUS SEARCH.")
                    search = input("INPUT EXIT IF USER WISHES TO TERMINATE SEARCH. ").lower()
                    if search == "exit":
                        print("Exiting...\n")
                        line()
                        break
                    else:
                        print("Exit Command = FALSE. Insure there are no spaces.\n")
                        line()

            # ------------------------------------------------------------------------------------------------------#

            case 3: # Items and Inventory
                line()
                print("\nYour body can only carry the scraps on your back.")
                print("Thus far you have collected:", player.scrapCount, "scraps.")
                print("You must collect", player.winScrap-player.scrapCount, "more before you can leave.\n")
                line()

            # ------------------------------------------------------------------------------------------------------#
            
            case 4: # Status and Health
                line()
                print("Your body has sustained",player.woundCount,"injuries.")
                print("The shell will die in", player.health, "more attacks.")
                print("Exercise caution when treading the sectors.\n")
                line()
            
            # ------------------------------------------------------------------------------------------------------#

            case _:
                line()
                print("\nIssued command returned as file-type - UNKNOWN. Reissue the command.\n")
                line()
                




# Win and Lose Conditions. This is where the game is at baby.

line()
print("\nWARNING THIS GAME IS STUPIDLY HARD. DOWNRIGHT UNFAIR.\n")
input("If you understand that you are not going to have a good time. Press anything. You can't leave anyways.")
line()

print("\n" * 100)

line()
print("\nWelcome to the wasteland Shepard.")
input("\nEnter to continue.")
print("\nYou have been selected by the Joint Community of Sector-090.")
print("Your only mission is to simply grab scrap.")
input("\nEnter to continue.")
print("\nWe of the council have deemed it necessarry for you to do this as our reserves are running out. Consider yourself lucky.")
print("Your scrap quota is", player.winScrap,"scrap, you cannot return until the quota is done.")
input("\nEnter to continue.")
print("\nUse the Travel Map to move between areas.")
print("Use the Search Function on your shell to locate and retrieve potential scrap.")
print("Your shell is equipped with a built in abnormality sensor function. If it gets too high I suggest leaving the area. 150 percent is more than dangerous enough.")

input("\nEnter to continue.")
print("\nHowever do not move too much as you will overload the battery rendering your shell useless for travel until you find fuel.")

input("\nEnter to continue.")
print("\nGood luck Shepard. You are going to need it.")
input("\nEnter to continue.")
print("\n" * 100)
while player.scrapCount < player.winScrap and player.health > 0:
    options()

if player.scrapCount > player.winScrap and player.health > 0:
    print("Shell completed all tasks, rerouting to user.")
    print("You live for one more day, Shepard.")
    line()
    input("Press enter to exit.")
    print("\n" * 100)
    print("b̸̛̬̥͙̪̰̖̱͙̾̿͘Ư̷̜̠̮̞̐̈́́͒̑̏̊͛̚̕͘ͅt̴̡̡͈̖̬̮͆̕ ̶̹̘̗̯̳̳͈͔̠̓̈́̑͊T̶̡̯̰̜̰̻̼͜͝Ḩ̵̪͖͉̦̦̜̞̘̔͂͛̋͛͑̓͗̄̑̈̚͝ë̷̮̼͈͔̠͚̪͎̜́͛͘͝ͅ ̷̧̢̤̖͍͈̮͖̮̈́̒͂̔̒̒̈́̽͌͠͠Ş̵̢̤͔͈̻͈̘̦̤͔͙͚͂̈́̿̀͜E̵̡͙̘̜̯͔̳̦͕͑̑̀̔͋̈̉̍̈̾̚͝͝C̷̨̘̩̰͍͈̣̠͕̝̞̠̀̀̈́̏͜Ţ̷̮̣̞̬̤̎͊͂̄̚Ȏ̷͈̖͕̀̿̍̀̽̀̄͘̚R̴̠̐̄͂̾̎̔̒̉̅̇̀͊͘S̵̡̡̬͙̥̣̥̹͈͆̏̅̌̀́̈́͛̍͋͝ ̵̡͖̣͚̺̖̭̙̠͔͈̈̄͛̉̒͜͝W̵̱̟͆Í̸̧̧͔̻̺̗̼̙̟̙͗͊͐̄̊͌́̍͛̊̓̈͘͝L̵̨̢̺̰̺͇͚͕͈̤̮̾̿̈́̀̈́̓̈́̽̿͋̕̚͝L̷͓͕̩͙̋̽ ̴̨͕̗̻̳̥̗̯̩͆̂͒͗̆̑̄̂̃̕͠n̸̨̧̲̫̤͍̭̼̮̿̆̈͗͛̔͐ơ̸͈̮̦͐͂̏̔̅̑̏̃͑̃̍̚͘t̸͈͎͚͕͈͉̀̓̑̌̋͑́͋̐̚ ̷̱̣̿̎̈́̈́͊̃́̑̇̐̓̚͘͠͝b̷̞͆̀͗͑͆̓͛̑̚͠ȩ̵͓̞̣̥̽̏͊́͆͂͊͝ ̶̨̟̖͉̼̬̣͕̭̠͂̔͐͐̚ͅͅͅs̸̨̧͓̲͕̘͈͎͈̠̤̿̆͗́̄͌̂̀͛̆̀̈́̍o̴̜͍̥̬̜͚̦̣͎̘̺͈͙̐̊̏ͅͅ ̴̳͚̈̏̅̓̾̚F̸͍̬̙̯̊́͆̌̀̓̐Ỏ̸̡̪͇̤̲̬͚̹̪͚̦̤͜R̷̢̨̗̼̗̗͓̻̈̽̔͋́́̂ͅG̴̛̙͑͂͋͋̋̾̃͆͘̚̚͘Ḯ̷̛̳̩̼̩͔̦̞̮̫̭̃̉̓̀͒V̸̨̨̳̜̝͍̬͔̭̰̖̳̗̆̆̈́̀Į̵͓̘͎̗̙͉̭̥̜̜̆N̷̢͕̰̝̘̘͎̥̞̟͙̆͜͜ͅͅG̸̯̳͚̮͕̏̈́͒̀͐̑́͝")


elif player.health <= 0:
    line()
    print("\n" * 100)
    print("SHELL DESTROYED EXITING LINK BETWEEN USER")
    input("Press Enter to exit shell (WARNING NOT EXITING SHELL MAY LEAD TO DEATH.)")
    print()
    line()
    print("ERROR UNABLE TO EXIT")
    print("ERROR...ERROR...ERROR...ERROR...ERROR...ERROR...ERROR...ERROR...ERROR...ERROR...\n" * 100, )
    print("If your hand causes you to stumble, cut it off… it is better for you to enter life maimed than with two hands to go into hell, where the fire never goes out…where the worms that eat them do not die, and the fire is not quenched.")
    print()
    input("Press Enter, Shepard.")
    print("̸͖̜́͝M̴̠̘̃͆A̷̮̟͆R̷̥͖͝Ý̴͇̦...C̴̱͐̀ͅO̶̓͆͜͜D̷̖͉́̾E̸̜̘͘͝.̴̑̓ͅ.̵̢̔.̴͎̓M̴̠̘̃͆A̷̮̟͆R̷̥͖͝Ý̴͇̦..." * 100)

    print("The pouring out of the seven bowls of Gods wrath, including sores on those who worshiped the beast, the turning of the sea to blood, scorching heat from the sun, darkness, and the gathering of armies for battle at Armageddon.")