# Imports
import threading

# Defining variables
version = "0.0.1"
commands =["help", "list", "quit"]
players = []
index = 0

#Cool title
print("""
Welcome to...

 __   __  _______  _______  _     _  _______  _______  _______ 
|  |_|  ||       ||       || | _ | ||  _    ||       ||       |
|       ||    ___||   _   || || || || |_|   ||   _   ||    _  |
|       ||   |___ |  | |  ||       ||       ||  | |  ||   |_| |
|       ||    ___||  |_|  ||       ||  _   | |  |_|  ||    ___|
| ||_|| ||   |___ |       ||   _   || |_|   ||       ||   |    
|_|   |_||_______||_______||__| |__||_______||_______||___|  

The server for cewl gaem
Version """ + version)
# Command processor (needs some work)
def commandProcessorFunc():
    while True:
        currentCommand = input("Input command: ")
        if currentCommand == commands[0] :
            print("Hi! There isn't much to do here, but we're always working on new stuff! If you need help, please contact @thecybercatwastkn on discord.")
        elif currentCommand == commands[1] :
            if len(players) == 0 :
                jpOutput = "There are no players currently online."
            else :
                for player in players :
                    jpOutput = "Players online:\n"
                    jpOutput += player + "\n"
            print(jpOutput)
        elif currentCommand == commands[2] :
            print("Shutting down...")
            quit()
# Defining and starting threads
CommandProcessor = threading.Thread(target=commandProcessorFunc)
CommandProcessor.start()

