text_file = 'test.txt'

def read_file(text_file):

    '''
    Functoin that reads a text file and returns the data from the text file

    Raises:
        FileNotFoundError : If it cannot find the file
    '''

    try:
        with open(text_file, 'r') as handle:

            data = handle.read()

            return data

    except FileNotFoundError:

        return None

def word_count(word):

    '''
    Function that counts the number of times a word is used
    '''

    with open(text_file,'r') as handle:

        data = handle.read()

        counter = 0

        for item in data.split():

            if item == word:

                counter += 1
        return counter

def line_count():

    '''
    Function that counts the number of lines in the text file
    '''

    with open(text_file,'r') as handle:

         data = handle.readlines()

         return len(data)

def longest_word():

    '''
    Function that gets the lonest word in the text file
    ''' 

    with open(text_file,'r') as handle:

        data = handle.read()

        long_word = ''

        for word in data.split():

            if len(list(word)) > len(list(long_word)):

                long_word = word

        return long_word




