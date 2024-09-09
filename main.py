# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# import pandas
#
# # Read the CSV file and create the phonetic dictionary
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
#
# # Function to convert a word to its phonetic representation
# def convert_to_phonetic(word):
#     try:
#         # Convert the input word to uppercase and generate the phonetic output list
#         output_list = [phonetic_dict[letter] for letter in word]
#         return output_list
#     except KeyError:
#         # Handle the case where a letter is not in the phonetic dictionary
#         print("Sorry, only letters in the alphabet are allowed.")
#         return None
#
# # Input from user
# word = input("Enter a word: ").upper()
#
# # Validate input and print the phonetic representation
# if word.isalpha():
#     result = convert_to_phonetic(word)
#     if result:
#         print(result)
# else:
#     print("Invalid input. Please enter only letters.")

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry ,only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()

