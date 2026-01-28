import unittest
from functions import is_even

class TestFunctions(unittest.TestCase):

    def test_is_even_empty(self):
        my_list, message = is_even([])
        self.assertEquals(my_list,[])
        self.assertEquals(message,"success")

if __name__ == '__main__':
    unittest.main()