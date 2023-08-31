#file = open("day-24/my_file.txt")
#contents = file.read()
#print(contents)
#file.close()

#with open("day-24/my_file.txt") as file:
#    contents = file.read()
#    print(contents)

#with open("day-24/my_file.txt", mode="a") as file:
#    file.write("\nNew text.")

#with open("/Users/gerzi/Desktop/my_file.txt") as file: #absolute path
#    contents = file.read()
#    print(contents)


with open("../../../../gerzi/Desktop/my_file.txt") as file: #relative path o ../ é usado para voltar uma pasta.
    contents = file.read()
    print(contents)