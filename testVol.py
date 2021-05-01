import unittest
import volCube

class TestCase(unittest.TestCase):
    #passing test
    def test_normal(self):
        self.assertEqual(volCube.volume(1,2,3),6)
    #negative test
    def test_neg(self):
        self.assertEqual(volCube.volume(1,2,-3),-6)
    #type error
    #def test_type(self):
    #    self.assertEqual(volCube.volume("1",2,-3),-6)
    #complex number
    def test_complex(self):
        self.assertEqual(volCube.volume(1.5,2,3),9)
if __name__ == '__main__':
    unittest.main()