from main import check
import unittest

class TestAOC(unittest.TestCase):
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
        self.assertEqual([2,0,0,0,99], check([1,0,0,0,99]))
        self.assertEqual([2,3,0,6,99], check([2,3,0,3,99]))
        self.assertEqual([2,4,4,5,99,9801], check([2,4,4,5,99,0]))
        self.assertEqual([30,1,1,4,2,5,6,0,99], check([1,1,1,4,99,5,6,0,99]))

if __name__ == '__main__':
    unittest.main()
