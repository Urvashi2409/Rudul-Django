def count_word_occurences(mystr):
    # We use lower function so that "This" matches with "this" 
    # Basically we ignore the uppercase and lowercase characters and focus on matching the words
    mystr = mystr.lower()
    punctuation_marks = '''!@#$%^&*()_+=-{}[]<>/,.?~'":;'''
    # Iterating through all the punctuation and finding thme in the myr and replacing those with nothing
    for char in punctuation_marks:
        mystr = mystr.replace(char, "")
    
    # Converting the string into list of words by spliting the string by spaces
    words = mystr.split()

    # Unique_words list will contain all the unique words from mystr
    unique_words = []

    # Words_counts list will contain the frequency of every unique word in mystr
    word_counts = []

    # Iterating in every word of the string
    for word in words:

        # Checkin if the word is already present in unique_words list
        if word in unique_words:

            # if it is present in unique_words list then get its index and increment the word_count of that particular word
            index = unique_words.index(word)
            word_counts[index] += 1
        else:

            # If it not present in the unique_words, then add it in the unique words
            # and because we are encounting this word first time so its word_count is also assigned as 1
            unique_words.append(word)
            word_counts.append(1)

    return unique_words, word_counts


# Taking the string as input
mystr = input("Please enter a string: ")

# Taking words and their count from count_word_occurences function
words, counts = count_word_occurences(mystr)

# count_word_occurences(mystr)

print("word occurences:")


# When we want to loop trough two lists, two tuples, two strings together then we use zip and put them in zip function
for word, count in zip(words, counts):
    print(f"{word}:{count} times")


# Topics which we revised through this project:

# 1. How to make a function and call it
# 2. Function can return multiple values and we can take these multipe values outside the function
# 3. Lower function to convert the string into lowercase
# 4. How to remove punctuation marks from the string by using replace function and replacing punctuation marks with nothing
# 5. Split function to split all the words inside the string
# 6. For loops to iterate through all the words in words list
# 7. Conditional statements (if/else) to check if a word is present in unique_words list or not
# 8. How to use different operators like membership (in), assignment (=, +=)
# 9. Index function to find the index of a word present in a list
# 10. Append function to add an element at the end of the list
# 11. Input function to take the input from user
# 12. Zip function to use single for loop to iterate in  multipe lists, tuples, strings
# 13. f string to print strings, numbers, variables, everything inside the same quotations by putting variables in the {}