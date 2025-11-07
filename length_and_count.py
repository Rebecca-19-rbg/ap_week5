def len_and_coun():

    # Length and Count:
    # a. Calculate the number of characters (including spaces and punctuation) in the word/
    phrase = "Supercalifragilisticexpialidocious"
    character_count = len(phrase)
    print(character_count)


    # b. Count the number of times the letter 'i' appears in the same word/phrase.

    letter_to_count = 'i'

    # Count the occurrences of the letter
    count = phrase.count(letter_to_count)

    # Print the result
    print(f"The letter '{letter_to_count}' appears {count} times in the phrase.")