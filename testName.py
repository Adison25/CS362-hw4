import unittest
import name

class TestCase(unittest.TestCase):
    #passing test
    def test_normal(self):
        self.assertEqual(name.full("adison", "emerick"),"adison emerick")
    #fail test
    #def test_fail(self):
    #    self.assertEqual(name.full("adison", "emerick"),"adisonemerick")
    #fail type test
    #def test_fail(self):
    #    self.assertEqual(name.full("adison", 0),"adison0")
if __name__ == '__main__':
    unittest.main()