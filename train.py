import datamanager

print("Welcome to the Trash-o-matic AI trainer")
while True:
    userinput = input("Enter the name of a piece of trash > ")
    userinput = userinput.lower()
    userinput = userinput.replace(" ", "_")
    while True:
            userinput2 = input("Please enter the number of where it belongs: \n1 = compost\n2 = bottles/cans\n3 = paper\n4 = trash\n5 = plastic\n> ")
            if userinput2 == "1":
                datamanager.save(userinput, "compost")
                print("Thanks for contributing to my database!")
                break
            elif userinput2 == "2":
                datamanager.save(userinput, "bottles/cans")
                print("Thanks for contributing to my database!")
                break
            elif userinput2 == "3":
                datamanager.save(userinput, "paper")
                print("Thanks for contributing to my database!")
                break
            elif userinput2 == "4":
                datamanager.save(userinput, "trash")
                print("Thanks for contributing to my database!")
                break
            elif userinput2 == "5":
                datamanager.save(userinput, "plastic")
                print("Thanks for contributing to my database!")
                break
            else:
                print("That wasn't one of the options, please try again")
            continue