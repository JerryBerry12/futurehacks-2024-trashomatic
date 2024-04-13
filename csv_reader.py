import datamanager

print("Enter the path to your csv file.")
filename = input("> ")
file1 = open(filename, 'r')
count = 0

for line in file1:
    line = line.rstrip()
    list = line.split(",")
    trash = list[0]
    number = list[1]
    trash = trash.lower()
    trash = trash.replace(" ", "_")
    if number == "1":
      textvalue = "compost"
    elif number == "2":
      textvalue = "bottles/cans"
    elif number == "3":
      textvalue = "paper"
    elif number == "4":
      textvalue = "trash"
    elif number == "5":
      textvalue = "plastic"
    else:
      print("Error! Your csv file is most likely corrupted or misformatted.")
      exit()
    datamanager.save(trash, textvalue)
    count = count + 1

count = int(count)
print("Successfully imported")
print(count)
print("pieces of trash!")