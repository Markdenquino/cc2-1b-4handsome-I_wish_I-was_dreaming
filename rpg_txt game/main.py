import tools
import settings
import keyboard
import time
import os
import sys


tools.clr_scrn()
tools.loading_screen()
print("\nLoading complete!")
time.sleep(2)


# Menu
def display_menu(selected_option):
    tools.clr_scrn()
    print("MENU")
    options = ["Start", "Quit"]

    for i, option in enumerate(options, start=1):
        if i == selected_option:
            print(f"\033[1;37;44m{i}. {option}\033[0m")  # Highlighted option
        else:
            print(f"{i}. {option}")

def main():
    selected_option = 1
    display_menu(selected_option)

    while True:
        event = keyboard.read_event(suppress=True)
        
        if event.event_type == keyboard.KEY_DOWN:
            
            if event.name == 'up' and selected_option > 1:
                selected_option -= 1
                display_menu(selected_option)
            
            elif event.name == 'down' and selected_option < 2:
                selected_option += 1
                display_menu(selected_option)
            
            elif event.name == 'enter':
                
                if selected_option == 1:
                    tools.clr_scrn()
                    settings.intro_a()
                    
                    opt = ("a", "b")
                    opts = None

                    while opts not in opt:
                        print("------------------------------------------------")
                        opts = input("Finish code (a) or Take a break (b): ")
                        
                        if opts not in opt: 
                            print("Invalid")
                        elif opts == "a":
                            tools.clr_scrn()
                            settings.finish_code()
                            break
                        elif opts == "b":
                            tools.clr_scrn()
                            settings.take_break()
                            time.sleep(1)

                        tools.clr_scrn()
                        settings.intro_b()
                        print("------------------------------------------------")
                        opts = input("Investigate (a) or Ignore (b): ")

                        if opts not in opt: 
                            print("Invalid")
                        elif opts == "a":
                            tools.clr_scrn()
                            settings.investigate()
                            break
                        elif opts == "b":
                            tools.clr_scrn()
                            settings.ignore()
                
                elif selected_option == 2:
                    tools.clr_scrn()
                    print("Suck my kaka!!")
                    break


if __name__ == "__main__":
    main()
