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

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You have no weapons, while the squirrel has a sword. You seem to be at a disadvantage.")
    print("..?")
    print("What a foolish thought. You are a human. Your opponent is a squirrel. You feel insulted that the squirrel even challenged you.")
    print("Fueled by rage, you agree to the duel.")
    print("...")

def center_path():
    print("You walk forward and find a abnormally large tree with a door on its trunk.")
    print("You open the door, and enter the tree to find only a warm, cozy bed inside.")
    print("You are tired and confused. You decide to close the door and sleep in the bed.")
    print("You wake up again. This time, however, you find yourself in your childhood bedroom.")
    print("It was all a dream.")
    print("Right?")

if __name__ == "__main__":
    intro()
