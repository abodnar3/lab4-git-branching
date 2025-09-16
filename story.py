def intro():
    print("You wake up in a dark forest. You can go left, forward, or right.")
    choice = input("Which direction do you choose? (left/center/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You try to pull out the sword, and it surprisingly slips right out. It feels warm.")
    print("Suddenly, your vision gets blurry. Your eyelids become heavy. You fall unconscious.")
    print("You wake up again. This time, however, in front of a small village occupied by squirrels.")
    print("The squirrels are ringing the town bells and scrambling with fear. One yells 'The beast is approaching!!'")
    print("You turn around, only to be met with an abnormally large cat. It is hissing and drooling. It sees you as an appealing appetizer.")
    print("Its eyes glare at you with murderous intent. You lift your sword and prepare for a grueling fight.")
    print("...")
    print("After many slashes and scratches, the fight is over. You stand victorious. The squirrels are in shock.")
    print("You are a hero. You slayed the beast who tormented the squirrel village for thousands of years.")
    print("The squirrels bake you a cookie for your efforts.")
    print("Yay!")


def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You walk forward and find a abnormally large tree with a door on its trunk.")
    print("You open the door, and enter the tree to find only a warm, cozy bed inside.")
    print("You are tired and confused. You decide to close the door and sleep in the bed.")
    print("You wake up again. This time, however, you find yourself in your childhood bedroom.")
    print("It was all a dream.")
    print("Right?")

if __name__ == "__main__":
    intro()
