from main import check
import unittest

class TestAOC2019_04(unittest.TestCase):
    def test_examples(self):
        self.assertEqual([99], check([99]))
        self.assertEqual([1, 2, 0, 1, 99], check([1, 0, 0, 1, 99]))
        self.assertEqual([
            3500,9,10,70,
            2,3,11,0,
            99,
            30,40,50
        ], check([
            1,9,10,3,
            2,3,11,0,
            99,
            30,40,50
        ]))

if __name__ == '__main__':
    unittest.main()
