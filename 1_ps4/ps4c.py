 # Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
# Late Days Used: x

import json
from ps4b import PlaintextMessage, EncryptedMessage # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]

def get_story_pads():
    """
    Returns: pads used to encrypt story.
    """
    with open('pads.txt') as json_file:
        return json.load(json_file)

WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###

def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a ciphertext and a list of possible pads used to create it,
    find the pad used to create the ciphertext

    We will consider the pad used to create the ciphertext as the pad
    that results in a plaintext with the most valid English words

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might
        have been used to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    word_list = load_words(WORDLIST_FILENAME)
    best_decrypted_text = None
    best_pad = None
    max_valid_word_count = 0

    for pad in pads:
        # Decrypt the ciphertext using the current pad
        decrypted_text = ciphertext.decrypt_message(pad).get_text()

        # Split the decrypted text into words
        words = decrypted_text.split()

        # Count how many valid English words are in the decrypted text
        valid_word_count = sum(1 for word in words if is_word(word_list, word))

        # Update the best result if needed
        if valid_word_count > max_valid_word_count:
            max_valid_word_count = valid_word_count
            best_decrypted_text = decrypted_text
            best_pad = pad

    if best_decrypted_text is None:
        best_pad = pads[-1]

    return PlaintextMessage(best_decrypted_text, best_pad)

def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    word_list = load_words(WORDLIST_FILENAME)
    story_text = get_story_string()
    possible_pads = get_story_pads()

    # Create an EncryptedMessage from the story text
    story_ciphertext = EncryptedMessage(story_text)

    # Decrypt the story using the possible pads
    decrypted_story = decrypt_message_try_pads(story_ciphertext, possible_pads, word_list)

    return decrypted_story.get_text()

if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    # story = decode_story()
    # print("Decoded story: ", story)

    # # This test is checking encoding a lowercase string with punctuation in it.
    # plaintext = PlaintextMessage('hello! ', [2, 0, 1, 4, 3, 36])
    # print('Expected Output: jemprE')
    # print('Actual Output:', plaintext.get_ciphertext())

    # # This test is checking decoding a lowercase string with punctuation in it.
    # encrypted = EncryptedMessage('jemprE')
    # print('Expected Output:', 'hello!')
    # print('Actual Output:', encrypted.decrypt_message([2, 0, 1, 4, 3, 36]).get_text())
    pass
