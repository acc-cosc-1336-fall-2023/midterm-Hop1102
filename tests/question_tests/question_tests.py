#write function tests here, don't add input('') statements here!
import unittest
import random

#follow this example to add questions b, c, and d for testing including their functions
#from src.question_a.question_a import get_random_number, test_config
from src.question_d.question_d import get_sum_of_evens, test_config
#from src.question_c.question_c import get_day_of_week, test_config
#from src.question_b.question_b import get_bonus_pay, test_config


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


def test_get_day_of_week():
    assert get_day_of_week(0) == "Invalid"
    assert get_day_of_week(1) == "Monday"
    assert get_day_of_week(2) == "Tuesday"
    assert get_day_of_week(3) == "Wednesday"
    assert get_day_of_week(8) == "Invalid"

if __name__ == '__main__':
    test_get_day_of_week()

def test_get_sum_of_evens():
    assert get_sum_of_evens(11) == 30
    assert get_sum_of_evens(10) == 30
    assert get_sum_of_evens(8) == 20

if __name__ == '__main__':
    test_get_sum_of_evens()
