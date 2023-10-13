#write function tests here, don't add input('') statements here!
import unittest
import random

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_random_number, test_config


class Test_Config(unittest.TestCase):

def test_question_a_config(self):
    self.assertEqual(True, test_config())

class TestRandomNUmber(unittest.TestCase):

    def test_get_random_number(self):
        random_number = get_random_number()
        self.assertTrue(1 <= random_number <= 5, f"Random number {random_number} is not between 1-5")

if __name__ == '__main__':
    unittest.main() 