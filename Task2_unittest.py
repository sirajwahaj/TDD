'''
    Student shall write their names here
        1. Student 1
        2. Student 2
'''

import unittest
from Task2 import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        """
        You can start with the sample text below but please feel free to add more text to cover all scenarios.
        """
        self.sample_text = (
            "Hello! This is a sample text 1. "
            "Contact us at example@example.com. Python is awesome. "
            "The python programming language is widely used. "
            "#Python #NLP check out https://example.com."
        )
        self.tp = TextProcessor(self.sample_text)


    """
        One example case test case is provided below but the implmentation of the function is missing to get you
        going with the TDD. Please note the test case will fail without implementation of the function in task2.py. 
        You will see an assertion error AssertionError: None != 'hello! this is a sample text 1. contact [130 chars]com.'. 
        The error will go away once you implement the function.
    """
    #TC for User story no 1 - This will fail!

    def test_convert_to_lowercase(self):
        expected = (
            "hello! this is a sample text 1. "
            "contact us at example@example.com. python is awesome. "
            "the python programming language is widely used. "
            "#python #nlp check out https://example.com."
        )
        self.assertEqual(self.tp.convert_to_lowercase(), expected)

    def test_extract_emails(self):
        expected = ["example@example.com"]
        self.assertEqual(self.tp.extract_emails(), expected)

    def test_find_and_count_hashtags(self):
        result, count = self.tp.find_and_count_hashtags()
        expected = ['#Python', '#NLP']  
        self.assertEqual(sorted(result), sorted(expected))  
        self.assertEqual(count, 2)

    def test_identify_and_list_urls(self):
        expected = ["https://example.com"]
        self.assertEqual(self.tp.identify_and_list_urls(), expected)

    def test_average_word_length(self):
        expected = 5.54  
        self.assertAlmostEqual(self.tp.average_word_length(), expected)

    def test_top_3_most_frequent_words(self):
        expected = [("is", 3), ("python", 3), ("hello", 1)]  
        self.assertEqual(self.tp.top_3_most_frequent_words(), expected)

    def test_find_longest_word(self):
        expected = "programming"  
        self.assertEqual(self.tp.find_longest_word(), expected)

    def test_sentences_with_python(self):
        expected = ['Python is awesome', 'The python programming language is widely used', '#Python #NLP check out https://example']
        self.assertEqual(self.tp.sentences_with_python(), expected)

    def test_remove_punctuation_and_special_characters(self):
        expected = (
            "Hello This is a sample text 1 "
            "Contact us at exampleexamplecom Python is awesome The python programming language is widely used "
            "Python NLP check out httpsexamplecom"
        )
        self.assertEqual(self.tp.remove_punctuation_and_special_characters(), expected)

    def test_convert_numbers_to_words(self):
        expected = (
            "Hello! This is a sample text one. "
            "Contact us at example@example.com. Python is awesome. The python programming language is widely used. "
            "#Python #NLP check out https://example.com."
        )
        self.assertEqual(self.tp.convert_numbers_to_words(), expected)



if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    """
    To generate an HTML report
    coverage run -a --branch Task1_Unittest_rover.py 
    coverage run -a --branch Task2_unittest.py 
    coverage report -m
    coverage html
    """
