from randomattack import random_attack

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.gold = 1000


    #Modify the attack() method to deal random damage within a range. I defined the range as +/-25%
    def attack(self, opponent):
        random_attack_amt = round(random_attack(self.attack_power),0)
        opponent.health -= random_attack_amt
        print(f"\n{self.name} attacks {opponent.name} for {random_attack_amt} damage!")
        print(f"{opponent.name} has {opponent.health} health remaining!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")


    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        self.health = min(self.max_health, self.health+25)
        print(f"{self.name} has had health restored to {self.health}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def special_ability(self, opponent):
        print(f"\n{self.name}'s Special Abilities:")
        print("1. Power Attack (Deals significant damage)")
        print("2. Second Wind (Heal yourself for 20 HP)")
        choice = input(f"Choose an ability for {self.name} (1 or 2): ").strip()

        if choice == '1':
            # Power Attack
            damage = round(self.attack_power * 1.25)
            opponent.health -= damage
            print(f"\n{self.name} uses Power Attack on {opponent.name} dealing {damage} damage!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has been defeated!")
            else:
                print(f"{opponent.name} has {opponent.health} health remaining!")
        elif choice == '2':
            # Second Wind
            heal_amount = 20
            self.health = min(self.max_health, self.health + heal_amount)
            print(f"\n{self.name} uses Second Wind, recovering {heal_amount} health. Current health: {self.health}/{self.max_health}")
        else:   
            # Technically a user can select a number other than 2 - might be an interesting place ot put 
            #cheats or secret capbilities
            print("Invalid choice. Performing a standard attack.")
            self.attack(opponent) # Fallback to normal attack

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
        self.focus_magic_active = False

    def special_ability(self, opponent):
        print(f"\n{self.name}'s Special Abilities:")
        print("1. Cast Spell (Deals high magical damage)")
        print("2. Focus Magic (Empowers your next spell)")
        choice = input(f"Choose an ability for {self.name} (1 or 2): ").strip()

        if choice == '1':
            # Cast Spell
            damage = self.attack_power * 1.5
            if self.focus_magic_active:
                damage *= 1.25  # 25% damage boost
                print(f"{self.name} channels focused magic!")
                self.focus_magic_active = False # Consume the focus
            
            damage = round(damage)
            opponent.health -= damage
            print(f"\n{self.name} casts a spell on {opponent.name} dealing {damage} damage!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has been defeated!")
            else:
                print(f"{opponent.name} has {opponent.health} health remaining!")
        elif choice == '2':
            # Focus Magic
            self.focus_magic_active = True #No further logic for Focus Magic is built out nor how to store prep information for the next round
            print(f"\n{self.name} begins to Focus Magic for the next spell!")
        else:
            print("Invalid choice. Performing a standard attack.")
            self.attack(opponent) # Fallback

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=45) 

    #abilities to shoot arrows and evade attacks.
    #"Quick Shot" (double arrow attack) and "Evade" (evades the next attack ).
    def special_ability(self, opponent):
        print(f"\n{self.name}'s Special Abilities:")
        print("1.Quick Shot")
        print("2.Evade")
        action = input("Which abiliity would you like to use? ")
        
        if action == '1':
            #ability: Quick Shot -> significant damage
            damage = self.attack_power * 1.5
            opponent.health -= damage
            print(f"\n{self.name} lands two arrows into the {opponent.name} dealing {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
            else:
                print(f"{opponent.name} has {opponent.health} health remaining!")
        elif action == '2':
            #ability: Evade -> avoid next attack from opponent
            self.health = min(self.health + 15, self.max_health)
            print(f"{self.name} deployes a divine sheild against {opponent.name}!")
        else:
            print("Invalid choice. Performing a standard attack.")
            self.attack(opponent) # Fallback


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=65) 

    #heal and shield against attacks.
    #"Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack).
    def special_ability(self, opponent):
        print(f"\n{self.name}'s Special Abilities:")
        print("1.Holy Strike")
        print("2.Divine Sheild")
        action = input("Which abiliity would you like to use? ")
        
        if action == '1':
            #ability: Holy Strike -> significant damage
            damage = self.attack_power * 1.75
            opponent.health -= damage
            print(f"\n{self.name} lands a Holy Strike attack {opponent.name} dealing {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
            else:
                print(f"\n{opponent.name} has {opponent.health} health remaining!")
        elif action == '2':
            #ability: StealDivine Sheild -> reduced next/current attack damage
            self.health = min(self.health + 10,self.max_health) #assume a reduciton of 10 points Wizzard damage
            print(f"{self.name} deployes a divine sheild against {opponent.name}!")
        else:
            print("Invalid choice. Performing a standard attack.")
            self.attack(opponent) # Fallback


class Rogue(Character): # Corrected typo: Rougue -> Rogue
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30) # Corrected super call

    def special_ability(self, opponent):
        print(f"\n{self.name}'s Special Abilities:")
        print("1.Backstab")
        print("2.Steal")
        action = input("Which abiliity would you like to use? ")

        if action == '1':
            #ability: Backstab -> significant damage
            damage = self.attack_power * 2
            opponent.health -= damage
            print(f"\n{self.name} sneaks behind {opponent.name} and stabs him in the back for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
            else:
                print(f"{opponent.name} has {opponent.health} health remaining!")
        elif action == '2':
            #ability: Steal -> take gold
            amounttosteal = 200
            self.gold += amounttosteal
            opponent.gold -= amounttosteal
            print(f"{self.name} sneaks behind {opponent.name} and steals {amounttosteal} gold!")
        else:
            print("Invalid choice. Performing a standard attack.")
            self.attack(opponent) # Fallback


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
