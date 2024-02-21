# 6.100A Fall 2023
# Problem Set 3
# Name: Rafael Moreno Ribeiro
# Collaborators: Jair Santana

"""
Description:
    Computes the similarity between two texts using two different metrics:
    (1) shared words, and (2) term frequency-inverse document
    frequency (TF-IDF).
"""

import string
import math
import re

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 1: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    # Use .split() method to generate a list of strings, each string being originally separated by a blank space
    list = input_text.split()
    return list
    pass


### Problem 2: Get Frequency ###
def get_frequencies(word_list):
    """
    Args:
        word_list: list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a word in l and the corresponding int
        is the frequency of the word in l
    """
    # Create an empty dictionary
    dict = {}

    # Add words and their frequencies to the dictionaries
    for word in word_list:
        freq = word_list.count(word)
        dict[word] = freq
    return dict

    pass


### Problem 3: Get Words Sorted by Frequency
def get_words_sorted_by_frequency(frequencies_dict):
    """
    Args:
        frequencies_dict: dictionary that maps a word to its frequency
    Returns:
        list of words sorted by decreasing frequency with ties broken
        by alphabetical order
    """
    # Use a custom sorting key
    # The negative sign in -frequency ensures that we are sorting in decreasing frequencies
    sorted_keys = sorted(frequencies_dict.items(), key=lambda item: (-item[1], item[0]))
    sorted_keys = [word for word, _ in sorted_keys]
    return sorted_keys
    pass


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          frequencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    # Start empty combined dictionary
    combined_dict = {}

    # Add frequencies to combined_dict
    for word, freq in dict1.items():
        combined_dict[word] = combined_dict.get(word, 0) + freq
    for word, freq in dict2.items():
        combined_dict[word] = combined_dict.get(word, 0) + freq

    # Find the maximum frequency
    max_frequency = max(combined_dict.values(), default=0)

    # Start a list with the most frequent words
    most_frequent_words = []

    # Find words with the maximum frequency and add them to the list
    for word, freq in combined_dict.items():
        if freq == max_frequency:
            most_frequent_words.append(word)

    # Organize alphabetically
    most_frequent_words.sort()

    return most_frequent_words
    pass


### Problem 5: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of words of text1
        dict2: frequency dictionary of words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums "frequencies"
        over all unique elements from dict1 and dict2 combined
        based on which of these three scenarios applies:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    # Create lists of the dictionary keys
    L1 = list(dict1.keys())
    L2 = list(dict2.keys())

    # Create string with all words in L1 and L2
    union = set(L1 + L2)

    # Define delta and sigma for each word, 0 if word not in dict
    def delta(word):
        return abs(dict1.get(word, 0) - dict2.get(word, 0))
    def sigma(word):
        return dict1.get(word, 0) + dict2.get(word, 0)

    # Initiate counting
    diff = 0
    all = 0
    for word in union:
        # Calculate every delta and add them
        diff += delta(word)
        # Calculate every sigma and add them
        all += sigma(word)

    # Round to two decimal places
    similarity = round(float(1-diff/all), 2)
    return similarity
    pass


### Problem 6: Finding TF-IDF ###
def get_tf(text_file):
    """
    Args:
        text_file: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculated as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    # Create list with all the words in the file as strings
    L = prep_data(load_file(text_file))

    # Get dictionary pairing words and their frenquencies
    word_freq = get_frequencies(L)

    # Find total number of words
    total_words = len(L)

    # Start empty dictionary that will match words and their TF
    word_tf = {}

    # Iterate word_freq to find each words' TF and store them
    for word, freq in word_freq.items():
        word_tf[word] = freq/total_words
    return word_tf
    pass


def get_idf(text_files):
    """
    Args:
        text_files: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()
    """
    # Initialize a dictionary to store word IDF values
    word_idf = {}

    # Calculate the total number of documents
    total_documents = len(text_files)

    # Create a set to keep track of documents containing each word
    word_document_count = {}

    # Iterate through the list of text file names
    for file_name in text_files:
        words = prep_data(load_file(file_name))
        unique_words = set(words)
        # Update word_document_count for each unique word in the document
        for word in unique_words:
            if word in word_document_count:
                word_document_count[word] += 1
            else:
                word_document_count[word] = 1

    # Calculate IDF for each word and store it in the dictionary
    for word, count in word_document_count.items():
        idf = math.log10(total_documents / count)
        word_idf[word] = idf

    return word_idf

def get_tfidf(text_file, text_files):
    """
    Args:
        text_file: name of file in the form of a string (used to calculate TF)
        text_files: list of names of files, where each file name is a string
        (used to calculate IDF)
    Returns:
       a sorted list of tuples (in increasing TF-IDF score), where each tuple is
       of the form (word, TF-IDF). In case of words with the same TF-IDF, the
       words should be sorted in increasing alphabetical order.

    * TF-IDF(i) = TF(i) * IDF(i)
    """
    # Create set containing all the words in the file, to avoid repetition
    word_set = set(prep_data(load_file(text_file)))

    # Generate dictionary maping each word to its TF
    word_tf = get_tf(text_file)

    # Generate dictionary maping each word to its IDF
    word_idf = get_idf(text_files)

    # Initiate list that will contain the tuples
    list = []

    # Iterate through every unique word, multiply its TF and IDF and add it to the list
    for word in word_set:
        tfxidf = word_tf[word]*word_idf[word]
        list.append((word, tfxidf))

    # Sort list, first considering TF-IDF, then alphabetical in case of a tie
    sorted_list = sorted(list, key=lambda item: (item[1], item[0]))
    return sorted_list

    pass


if __name__ == "__main__":
    pass
    # ##Uncomment the following lines to test your implementation
    # ## Tests Problem 1: Prep Data
    '''test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = prep_data(hello_world), prep_data(hello_friend)
    print(world) ## should print ['hello', 'world', 'hello', 'there']
    print(friend) ## should print ['hello', 'friends']'''

    # ## Tests Problem 2: Get Frequencies
    '''world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq) ## should print {'hello': 2, 'world': 1, 'there': 1}
    print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}'''

    # ## Tests Problem 3: Get Words Sorted by Frequency
    '''world_words_sorted_by_freq = get_words_sorted_by_frequency(world_word_freq)
    friend_words_sorted_by_freq = get_words_sorted_by_frequency(friend_word_freq)
    print(world_words_sorted_by_freq) ## should print ['hello', 'there', 'world']
    print(friend_words_sorted_by_freq) ## should print ['friends', 'hello']'''

    # ## Tests Problem 4: Most Frequent Word(s)
    # freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    # most_frequent = get_most_frequent_words(freq1, freq2)
    # print(most_frequent) ## should print ["hello", "world"]

    # ## Tests Problem 5: Similarity
    #test_directory = "tests/student_tests/"
    #hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    #world, friend = prep_data(hello_world), prep_data(hello_friend)
    #world_word_freq = get_frequencies(world)
    #friend_word_freq = get_frequencies(friend)
    #word_similarity = calculate_similarity_score(world_word_freq, friend_word_freq)
    #print(word_similarity)        # should print 0.33

    # ## Tests Problem 6: Find TF-IDF
    #text_file = 'tests/student_tests/hello_world.txt'
    #text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    #tf = get_tf(text_file)
    #idf = get_idf(text_files)
    #tf_idf = get_tfidf(text_file, text_files)
    #print(tf) ## should print {'hello': 0.5, 'world': 0.25, 'there': 0.25}
    #print(idf) ## should print {'there': 0.3010299956639812, 'world': 0.3010299956639812, 'hello': 0.0, 'friends': 0.3010299956639812}
    #print(tf_idf) ## should print [('hello', 0.0), ('there', 0.0752574989159953), ('world', 0.0752574989159953)]
