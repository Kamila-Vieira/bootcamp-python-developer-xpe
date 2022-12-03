import unittest
from root_square_solver import rootSquareSolver

class CheckRootSquareSolver(unittest.TestCase):
  
  def test_checkTwoRoots(self):
    response = rootSquareSolver(1, -5, 6) # x² - 5 + 6 => r¹= 3 & r² = 2
    self.assertEqual(len(response), 2)
    
  def test_checkRootFirstValue(self):
    response = rootSquareSolver(1, -5, 6)
    self.assertIn(response[0], [2, 3])
    
  def test_checkRootSecondValue(self):
    response = rootSquareSolver(1, -5, 6)
    self.assertIn(response[1], [2, 3])
    
  def test_checkOneRoot(self):
    response = rootSquareSolver(1, -4, 4) # x² - 4 + 4 => r¹= 2
    self.assertEqual(len(response), 1)
    
  def test_checkWithoutCoefficients(self):
    response = rootSquareSolver()
    self.assertEqual(response, None)
    
  def test_checkNegativeDelta(self):
    response = rootSquareSolver(1, 2, 3)
    self.assertEqual(response, None)
    
  def test_checkWithoutACoefficient(self):
    response = rootSquareSolver(b=1,c=3)
    self.assertEqual(response, None)
    
  def test_checkWithoutBCoefficient(self):
    response = rootSquareSolver(a=1,c=3)
    self.assertEqual(response[0] * -1, response[1])
    
  def test_checkWithoutCCoefficient(self):
    response = rootSquareSolver(a=1,b=3)
    self.assertIn(0, response)
    
