import unittest
from algorithm import search

class TestSearch(unittest.TestCase):

  def setUp(self):
    self.array = [10, 5, 20, 30, 1, 4]

  def test_successful(self):
    self.assertTrue(search(2,10,self.array))

  def test_failed(self):
    self.assertFalse(search(40,50,self.array))

  def test_emptyArray(self):
    self.assertFalse(search(2,10,[]))
    
  def test_forNegativeNumber(self):
    self.assertFalse(search(-1,2,self.array))

  def test_equality(self):
    self.assertFalse(search(1,1,self.array))

if __name__ == '__main__':
    unittest.main()
