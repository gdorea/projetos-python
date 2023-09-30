import pandas

data = pandas.read_csv("./NATO project v2/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    try:
        word = input("Enter a word: ").upper()
        if type(word) == int():
            break
        else:
            output_list = [phonetic_dict[letter] for letter in word]
            print(output_list)
            break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
