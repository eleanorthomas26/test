##Still to do:
    #What to do with words where the ' is removed?
    #How to sort them into types of word?

## Import counter to calculate frequency and panda for the display
from collections import Counter
import pandas as pd
import nltk
from nltk.corpus import words
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

## Establish nested dictionary
word_dictionary = {}

## Function to check if a word is real
def is_real_word(word):
    valid_words = set(words.words())
    return word() in valid_words

##Allow user to input file name
filename = input('Please enter file name')

## Import text file
with open(filename, 'r') as file:
    #first read the file into a string
    content = file.read()
    #make the string all lower case
    content = content.lower()
    #remove any non-letter, non-spaces to clean the string
    content = ''.join(char for char in content if (char.isalpha() or char.isspace()))

## Spilt single string into individual words
words = content.split()


# Check if all the words are real, if not, ask user to enter replacement
for word in words:
    #Check word is real
    word_to_check = word
    if is_real_word(word_to_check) is True:
        return word
    else:
        new_word = word
        while is_real_word(word_to_check) is False:
            new_word = input('Please enter replacement word(s)')
            new_word = content.lower()
            new_word = ''.join(char for char in content if char.isalpha())
        return new_word

word_count = Counter(words)

## Create dictionary for the word with length and frequency
#Check if word alread in dictionary, if no then make entry
for word in words:
    if word not in word_dictionary: 
        length = len(word)
        frequency = word_count[word]
        dictionary_entry = {
            'length' : length,
            'frequency' : frequency}
       #Add this word to a nested dictionary 
        word_dictionary[word] = dictionary_entry

# convert nested dictionary to a table for visual ease
df = pd.DataFrame.from_dict(word_dictionary, orient='index')

print(df)