# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.

magic = "abracadabra"

print(magic[4])

# b. Retrieve the second to last character.

print(magic[1:])
# c. Find the first occurrence of the letter 'c'.

letter_find = magic.find("c")

print(letter_find)

# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# a. Extract the letters 'hij'.
print(alphabet[7:10])

# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])   #index can find things for you

# c. Reverse the entire string using slicing.
print(alphabet[::-1])       # <------   Reversing a string 

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote ="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[83:100])

# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective"
search_word = "subjective"

# Find the starting index of the word
start_index = info.find(search_word)

if start_index != -1:
    # Calculate the end index
    end_index = start_index + len(search_word)
    # Extract the word using slicing
    extracted_word = info[start_index:end_index]
    print(extracted_word)
else:
    print(f"'{search_word}' not found.")

# b. Extract every third word.


words = info.split()  # Split the string into a list of words
every_third_word = words[2::3]
print(every_third_word)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reverse = "subjective is Good good. is Fun fun. is Python"

print(reverse)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
text = "MAY THE FORCE BE WITH YOU."
print(text.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],

# a. Convert the list into a single string.
motto ="Make haste slowly."
# b. Now, split the string at every occurrence of the letter 'a'.
split_list = motto.split('a')
print(split_list)

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."

text =  "Life is what happens when you are busy making other plans."

new_text = text.replace("busy", "distracted")

even_newer_text = new_text.replace("plans", "mistakes")

print(even_newer_text)
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

text =  "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word_to_find = "moonlight"

if word_to_find in text:
    print(f"'{word_to_find}' is found in the text.")
else:
    print(f"'{word_to_find}' is not found in the text.")

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/
phrase = "Supercalifragilisticexpialidocious"
character_count = len(text)
print(character_count)


# b. Count the number of times the letter 'i' appears in the same word/phrase.

letter_to_count = 'i'

# Count the occurrences of the letter
count = phrase.count(letter_to_count)

# Print the result
print(f"The letter '{letter_to_count}' appears {count} times in the phrase.")