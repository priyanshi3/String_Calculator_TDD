import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    # Test that an empty string returns 0
    def test_empty_string(self):
        self.assertEqual(add(""), 0)  

    # Test that a single number in a string returns that number
    def test_single_number(self):
        self.assertEqual(add("1"), 1)  
        
    # Test that two numbers separated by a comma return their sum
    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 4)  

    # Test that handle delimiter 
    def test_custom_separator(self):
        self.assertEqual(add("//;\n1;2"), 3)  
        
    # Test that an error is raised when a negative number is encountered
    def test_negative_numbers(self):
        try:
            add("-1")
            self.fail("Expected ValueError to be raised")
        except ValueError as e:
            self.assertEqual(str(e), "Negative numbers not allowed: -1 ")
            
    # Test that multiple negative numbers raise an error
    def test_multiple_negative_numbers(self):
        try:
            add("-1,-2,3")
            self.fail("Expected ValueError to be raised")
        except ValueError as e:
            self.assertEqual(str(e), "Negative numbers not allowed: -1, -2")

    # Test that numbers greater than 1000 are ignored
    def test_numbers_bigger_than_1000(self):
        self.assertEqual(add("1001,2"), 3)  


class CustomTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        if result.failures:
            print("\nFailed cases:")
            for failure in result.failures:
                print(failure[0].id())
        return result


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringCalculator)
    CustomTestRunner(verbosity=2).run(suite)