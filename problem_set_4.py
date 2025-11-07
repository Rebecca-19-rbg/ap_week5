def problem4():

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