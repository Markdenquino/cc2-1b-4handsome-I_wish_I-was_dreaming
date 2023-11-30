import os
import time
import sys

# clear screen
def clr_scrn():
    os.system('cls' if os.name == 'nt' else 'clear') 

# slow print
def slow_print(txt, delay=0.05):
    for char in txt:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def slow_print_list(txt_list, delay=0.05):
    for txt in txt_list:
        slow_print(txt, delay)

# Loading screen
def loading_screen():
    total_iterations = 50  # Adjust the total number of iterations as needed

    for i in range(1, total_iterations + 1):
        progress = i / total_iterations
        bar_length = 50
        bar = int(progress * bar_length)
        loading_bar = f"\033[38;5;206m[{'=' * bar}{' ' * (bar_length - bar)}] {int(progress * 100)}%"
        
        sys.stdout.write('\r' + loading_bar)
        sys.stdout.flush()
        time.sleep(0.1)  # Adjust the sleep duration for the desired speed

if __name__ == "__main__":
    loading_screen()
    print("\nLoading complete!")


# Color

class TextColor:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    PINK = "\033[38;5;206m"