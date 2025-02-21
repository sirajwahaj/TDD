'''
    Student shall write their names here
        1. Sirajulhaq Wahaj
        2. Abdelhakim Mraihi
'''


import unittest
from Task1_Rover import rovar

class test_string(unittest.TestCase):
    '''
        _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
        _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
        Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

        Write your TCs based on the lab instructions. One TC has been written below as an example
        
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        cls.rv= rovar() 


    

    # You can continue writing your test cases here based on the assignment description

    def test_enrove_multiple_uppercase_consonants(self):  
        self.assertEqual(self.rv.enrove("DBCy"), "DODBOBCOCyoy")  
    
    def test_enrove_vowel(self):
        self.assertEqual(self.rv.enrove("äpple"), "äpoppoplole")

    
    # Example test case to check lower case rover
    def test_enrove_small(self):
        self.assertEqual(self.rv.enrove('b'), 'bob')

     # Test cases for enrove (encoding) method

    def test_enrove_null(self):
        '''
            Test encoding with null input.
        '''
        self.assertIsNone(self.rv.enrove(None))

    def test_enrove_empty_string(self):
        '''
            Test encoding with an empty string.
        '''
        self.assertEqual(self.rv.enrove(''), '')

    def test_enrove_lowercase_consonant(self):
        '''
            Test encoding with a lowercase consonant.
        '''
        self.assertEqual(self.rv.enrove('b'), 'bob')

    def test_enrove_uppercase_consonant(self):
        '''
            Test encoding with an uppercase consonant.
        '''
        self.assertEqual(self.rv.enrove('B'), 'BOB')

    def test_enrove_vowel(self):
        '''
            Test encoding with a vowel (should remain unchanged).
        '''
        self.assertEqual(self.rv.enrove('a'), 'a')

    def test_enrove_number(self):
        '''
            Test encoding with a number (should remain unchanged).
        '''
        self.assertEqual(self.rv.enrove('1'), '1')

    def test_enrove_special_character(self):
        '''
            Test encoding with a special character (should remain unchanged).
        '''
        self.assertEqual(self.rv.enrove('!'), '!')

    def test_enrove_mixed_string(self):
        '''
            Test encoding with a mixed string (consonants, vowels, numbers, special characters).
        '''
        self.assertEqual(self.rv.enrove('Hello123!'), 'HOHelollolo123!') # I just had to replace "o" with "O"

    def test_enrove_vowels(self):
        # Swedish vowels + 'y' (lowercase and uppercase)
        for vowel in ['a', 'e', 'i', 'o', 'u',  'å', 'ä', 'ö', 'A', 'E', 'I', 'O', 'U', 'Å', 'Ä', 'Ö']:
            self.assertEqual(self.rv.enrove(vowel), vowel)

    # Test cases for derove (decoding) method

    def test_derove_null(self):
        '''
            Test decoding with null input.
        '''
        self.assertIsNone(self.rv.derove(None))

    def test_derove_empty_string(self):
        '''
            Test decoding with an empty string.
        '''
        self.assertEqual(self.rv.derove(''), '')

    def test_derove_lowercase_consonant(self):
        '''
            Test decoding with a lowercase consonant.
        '''
        self.assertEqual(self.rv.derove('bob'), 'b')

    def test_derove_uppercase_consonant(self):
        '''
            Test decoding with an uppercase consonant.
        '''
        self.assertEqual(self.rv.derove('BOB'), 'B')

    def test_derove_vowel(self):
        '''
            Test decoding with a vowel (should remain unchanged).
        '''
        self.assertEqual(self.rv.derove('a'), 'a')

    def test_derove_number(self):
        '''
            Test decoding with a number (should remain unchanged).
        '''
        self.assertEqual(self.rv.derove('1'), '1')

    def test_derove_special_character(self):
        '''
            Test decoding with a special character (should remain unchanged).
        '''
        self.assertEqual(self.rv.derove('!'), '!')

    def test_derove_mixed_string(self):
        '''
            Test decoding with a mixed string (consonants, vowels, numbers, special characters).
        '''
        self.assertEqual(self.rv.derove('Helollolo123!'), 'Hello123!')
# Test cases for swedish vowels 





if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)