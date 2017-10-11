import unittest
import readfiles

class TestReadFiles(unittest.TestCase):

    '''
    Class to test the functions on the readfiles module

    Args:
        unittest.TestCase class from the unittest module to create unittest
    '''

    #  Check if data is gotten
    def test_get_data(self):

        '''
        Test case to confirm that we are getting data from the file
        '''

        with open('test.txt','r') as handle:

            data = handle.read()

            self.assertEqual( data, readfiles.read_file('test.txt') )

    def test_nonfile(self):

        '''
        Test to confirm that an exception is raised when a wrong file is inputted
        '''

        self.assertEqual( None, readfiles.read_file('tests.txt') )

    def test_times_word_used(self):

        '''
        Test to count how many times a word is used
        '''

        with open('test.txt','r') as handle:

            data = handle.read()

            counter = 0

            for word in data.split():

                if word == 'Lorem':

                    counter += 1

            self.assertEqual(counter, readfiles.word_count('Lorem'))

    def test_number_of_lines(self):

        '''
        Test to count the number of lines in the text file
        '''

        with open('test.txt','r') as handle:

            data = handle.readlines()

            self.assertEqual( len(data), readfiles.line_count() )

    def test_longest_word(self):

        '''
        Test to check the longest work
        '''

        with open('test.txt', 'r') as handle:

            data = handle.read()

            long_word = ''

            for word in data.split():

                if len(list(word)) > len((list(long_word))):

                    long_word = word

            self.assertEqual( long_word, readfiles.longest_word() )


if __name__ == '__main__':
    unittest.main()