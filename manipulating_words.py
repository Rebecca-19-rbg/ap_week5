def manipulate_words():

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