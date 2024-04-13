import datamanager
import time
# datamanager.save(key, name)
# datamanager.load(key)

global whereitgoes
global userinput
global userinput2
print("Loading Trash-o-matic...")
time.sleep(3)

while True:
    userinput = input("Enter the name of a piece of trash: ")
    userinput = userinput.lower()
    userinput = userinput.replace(" ", "_")
    if userinput == "quit" or userinput == "q" or userinput == "exit":
        exit()
    try:
        whereitgoes = datamanager.load(userinput)
        print("That piece of trash goes into: " + whereitgoes)
    except KeyError:
        print("Sorry, I don't know where that goes. Please train me more, so that I can learn!")
    