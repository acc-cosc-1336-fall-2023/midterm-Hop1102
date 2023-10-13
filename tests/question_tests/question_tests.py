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

def test_get_bonus_pay():
    assert get_bonus_pay(-1) == 'Invalid'
    assert get_bonus_pay(200) == 10
    assert get_bonus_pay(600) == 36
    assert get_bonus_pay(1000) == 70
    assert get_bonus_pay(1500) == 120
    assert get_bonus_pay(2000) == 'Invalid'

if __name__ == '__main__':
    test_get_bonus_pay()
    