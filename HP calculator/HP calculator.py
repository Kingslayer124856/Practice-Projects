"""
Title: Player HP Calculator
By: Cassandra King
Completed on: 1/10/23

Description:
Display players HP levels at 85p, player can take hits and heal.
Players HP can not go past max and once HP is 0 the player is dead

"""
# Add warning messages for when the player is at low HP
# Add Death saves once in the negatives 
Menu = ["(D)amage","(H)eal", "(R)est"]
MAX_HP = 85

def main():
    """The main is used to display the changing Current HP,
     aswell as to give the user a selection of what to do by using the menu"""
    current_hp = MAX_HP
    while current_hp > 0:
        print("Your Characters HP is currently: ", current_hp)
        for i in Menu:
            print(i)
        select = input("Please Select an option: ").upper()
        if select == "D":
            wt_hp = damage(current_hp)
        elif select == "H":
            wt_hp = heal(current_hp)
        elif select == "R":
            wt_hp = long_rest(current_hp)
        else:
            print("Please select a valid option")
        current_hp = wt_hp
    print("Your Character is dead")
    
def damage(hp):
    """Damage function is used to calculate the total hp left after damage was taken.
    Collecting the amount of damage taken and removing it from the current HP and returning that"""
    damage = int(input("How much damage did you recieve: "))
    update_hp = hp - damage 
    return update_hp

def heal(hp):
    """ Heal function is adding towards the players HP, 
    while making sure they do not exceed the Max HP and returning the change in HP"""
    potion = int(input("How much healing did you recieve: "))
    update_hp = min(hp + potion, MAX_HP) 
    return update_hp

def long_rest(hp):
    """ A long rest provides the player to 
    go back to the Max Hp which resets the players HP to the Max """
    update_hp = MAX_HP
    return update_hp

main()