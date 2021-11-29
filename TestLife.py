import unittest
from life import Life

class TestLife(unittest.TestCase):
    def setUp(self):
        self.p1 = Life()

    def testGetRemainingLives(self):
        self.assertEqual(self.p1.getRemainingLives(), 7)

    def testDecreaseLife(self):
        self.p1.decreaseLife()
        self.assertEqual(self.p1.getRemainingLives(), 6)


if __name__ =='__main__':
    unittest.main()