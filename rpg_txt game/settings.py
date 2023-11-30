import tools


# player
class player:
    def life():
        Life = 3
    def damage():
        Damage = life - 1

# Scenes

def intro_a():
    tools.txt_list = [f"{tools.TextColor.BLUE}It's late at night and you are sitting alone in your room,",
        f"finishing your code that's due tomorrow{tools.TextColor.RESET}"]
    tools.slow_print_list(tools.txt_list)


def finish_code():
    tools.txt_list = [f"{tools.TextColor.BLUE}You decided that you have to finish the code tonight-",
    "You picked up where you last left off and continued writing",
    f"-End of story{tools.TextColor.RESET}"]
    tools.slow_print_list(tools.txt_list)

def take_break():
    tools.txt_list = [f"{tools.TextColor.BLUE}Seeing that there's still much to do,",
    f"you decided to take a breather and get some fresh air outside{tools.TextColor.RESET}"]
    tools.slow_print_list(tools.txt_list)


def intro_b():
    tools.txt_list = [f"{tools.TextColor.BLUE}As you left your room,",
        f"creaking was heard on the floor boards down the hallway.{tools.TextColor.RESET}"]
    tools.slow_print_list(tools.txt_list)

def investigate():
    tools.txt_list = [
        f"{tools.TextColor.BLUE}Out of curioisty, you went closer to source of the noise.",
        "Once you scanned the area, you heard whispers above you.",
        "As you slowly looked up, a mangled corpse floating at the ceiling.",
        f"It drpos down with a spine chilling shriek... and you feinted.{tools.TextColor.RESET}"
    ]
    tools.slow_print_list(tools.txt_list)

def ignore():
    tools.txt_list = [
        f"{tools.TextColor.BLUE}You though it was nothing and proceed to make you way to the yard.",
        "However, you noticed something is off and felt an eerie that you are being followed.",
        "You slowly turned around and saw a man with missing eyes and a broken hanging jaw as his skins slowly decays.",
        f"He suddenly strangles you and you tried to gasp for air... then moments later, you feinted.{tools.TextColor.RESET}"
    ]
    tools.slow_print_list(tools.txt_list)


def encounters():
    pass