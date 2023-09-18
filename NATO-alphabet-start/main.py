student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

data_nato = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
nato_dict = {row.letter:row.code for (index, row) in data_nato.iterrows()}

#print(nato_dict)

#TODO 1. Create a dictionary in this format:


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

word_list = [nato_dict[letter] for letter in word]

print(word_list)