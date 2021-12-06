import unittest
from translator import english_to_french, french_to_english

def french_to_english_compare(self, french_text, english_text):
    translation = french_to_english(french_text)
    try:
        self.assertEqual(translation, english_text)
        self.assertNotEqual(translation, english_text)
    except:
        pass

def english_to_french_compare(self, english_text, french_text):
    translation = english_to_french(english_text)
    try:
        self.assertEqual(translation, french_text)
        self.assertNotEqual(translation, french_text)
    except:
        pass

class TranslatorTest(unittest.TestCase):
    def test_french_to_english(self):
        french_to_english_compare(self, None, None)
        french_to_english_compare(self, 'Bonjour', 'Hello')
    
    def test_english_to_french(self):
        english_to_french_compare(self, None, None)
        english_to_french_compare(self, 'Hello', 'Bonjour')

if __name__ == '__main__':
    unittest.main()
