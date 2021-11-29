import unittest
from guess import Guess

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.p1 = Guess(25)

    def testGuess(self):
        self.assertTrue(self.p1.guess(25))
        self.assertFalse(self.p1.guess(10))
        self.assertFalse(self.p1.guess(35))

    def testGetRecentRecord(self):
        self.p1.guess(10)
        self.assertEqual(self.p1.getRecentRecord(), "(Up)")
        self.p1.guess(35)
        self.assertEqual(self.p1.getRecentRecord(), "(Down)")

    def testGetSecretNumber(self):
        self.assertEqual(self.p1.getSecretNumber(), 25)

if __name__ == '__main__':
    unittest.main()