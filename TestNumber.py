import unittest
from number import Number

class TestNumber(unittest.TestCase):
    def setUp(self):
        self.p1 = Number()

    def testGetRandomNumber(self):
        self.assertGreaterEqual(50, self.p1.getRandomNumber(50))
        self.assertLessEqual(1, self.p1.getRandomNumber(50))


if __name__ =='__main__':
    unittest.main()
