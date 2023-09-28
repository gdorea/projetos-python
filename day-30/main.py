#FileNotFound

try:
    file = open("./day-30/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("./day-30/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")