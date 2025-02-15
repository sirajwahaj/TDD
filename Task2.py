import re
import string
from collections import Counter

class TextProcessor:
    def __init__(self, text):
        self.text = text
    '''
    The TC for User story 1 will fail as there is no implementation added. Add the implementation of your user stories below.
    '''

    def convert_to_lowercase(self):
        """Convert all characters in the text to lowercase."""
        return self.text.lower()

    def extract_emails(self):
        """Extract all email addresses mentioned in the text."""
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(email_pattern, self.text)

    def find_and_count_hashtags(self):
        """Find and count all unique hashtags in the document."""
        hashtag_pattern = r'#\w+'
        hashtags = re.findall(hashtag_pattern, self.text)
        return sorted(hashtags), len(hashtags)  


    def identify_and_list_urls(self):
        """Identify and list all URLs mentioned in the text."""
        url_pattern = r'https?://[^\s,!?]+'
        urls = re.findall(url_pattern, self.text)
        return sorted(set(url.rstrip(string.punctuation) for url in urls))

    def average_word_length(self):
        """Calculate the average word length in the document."""
        words = self.text.split()
        if not words:
            return 0
        total_length = sum(len(word.strip(string.punctuation)) for word in words)
        return round(total_length / len(words), 2)

    def top_3_most_frequent_words(self):
        """Determine the top 3 most frequent words in the text."""
        words = self.text.split()
        word_count = Counter()
        for word in words:
            # Normalize: remove punctuation and convert to lowercase
            cleaned_word = word.strip(string.punctuation).lower()
            if cleaned_word and cleaned_word.isalpha():  # Only count valid words
                word_count[cleaned_word] += 1
        return word_count.most_common(3)  # Get the top 3 most common words

    def find_longest_word(self):
        """Find the longest word in the text."""
        words = self.text.split()
        longest = ""
        for word in words:
            cleaned_word = word.strip(string.punctuation)
            # Exclude words that are URLs or non-alphabetic
            if cleaned_word.isalpha() and len(cleaned_word) > len(longest):
                longest = cleaned_word
        return longest

    def sentences_with_python(self):
        """Identify sentences that contain the word 'Python', case-insensitive."""
        sentences = re.split(r'[.!?]\s*', self.text)
        return [sentence.strip() for sentence in sentences if re.search(r'\bpython\b', sentence, re.IGNORECASE)]

    def remove_punctuation_and_special_characters(self):
        """Remove all punctuation and special characters from the text."""
        # Remove punctuation but preserve numbers and letters
        text_without_punctuation = re.sub(r'[^\w\s]', '', self.text)
        # Normalize whitespace to a single space
        text_no_extra_spaces = re.sub(r'\s+', ' ', text_without_punctuation)
        # Strip leading/trailing spaces
        cleaned_text = text_no_extra_spaces.strip()
        return cleaned_text



    def convert_numbers_to_words(self):
        """Convert numerical figures (1-10) into their written-out forms."""
        number_map = {
            '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
            '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'
        }

        # Function to replace a matched number with its word form
        def replace_number(match):
            return number_map[match.group()]

        # Replace numbers 1-10 with their word forms
        result_text = re.sub(r'\b(10|[1-9])\b', replace_number, self.text)
        return result_text

'''
if __name__ == '__main__':
    text = (
        "Hello! This is a sample text 1. "
            "Contact us at example@example.com. Python is awesome. "
            "The python programming language is widely used. "
            "#Python #NLP check out https://example.com."
    )
    tp = TextProcessor(text)
    print(tp.convert_numbers_to_words())
'''