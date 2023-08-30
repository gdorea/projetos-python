#file = open("day-24/my_file.txt")
#contents = file.read()
#print(contents)
#file.close()

with open("day-24/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("day-24/my_file.txt", mode="a") as file:
    file.write("\nNew text.")