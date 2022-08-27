bcolors = {}
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White
ENDC = '\033[0m'
class Text:
    def __init__(self, text, BOOLrainbow = False, color = None):
        if BOOLrainbow:
            R_color = 1
            for char in text:
                if R_color == 1:
                    print(Red, end="")
                elif R_color == 2:
                    print(Yellow, end="")
                elif R_color == 3:
                    print(Green, end="")
                elif R_color == 4:
                    print(Cyan, end="")
                elif R_color == 5:
                    print(Blue, end="")
                elif R_color == 6:
                    print(Purple, end="")
                    R_color = 1
                print(char, end="")
                R_color+=1
            R_color+=1
            print(ENDC)
        elif color:
            if color == "Black":
                print(Black + text + ENDC)
            if color == "Red":
                print(Red + text + ENDC)
            if color == "Green":
                print(Green + text + ENDC)
            if color == "Yellow":
                print(Yellow + text + ENDC)
            if color == "Blue":
                print(Blue + text + ENDC)
            if color == "Purple":
                print(Purple + text + ENDC)
            if color == "Cyan":
                print(Cyan + text + ENDC)
            if color == "White":
                print(White + text + ENDC)
def MAKE_TEXT(text, BOOLrainbow, color):
    Text(text, BOOLrainbow, color)
