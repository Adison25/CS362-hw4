import unittest
import avgList

class TestCase(unittest.TestCase):
    #passing test
    def test_normal(self):
        self.assertEqual(avgList.avg((1,2,3)),2)
    #negative test
    def test_empty(self):
        self.assertEqual(avgList.avg(()),0)
    #type error
    #def test_type(self):
    #    self.assertEqual(avgList.avg(("1",2,-3)),-6)
    #complex number
    #def test_complex(self):
    #    self.assertEqual(avgList.avg((1.5,2,3)),6.5)
if __name__ == '__main__':
    unittest.main()