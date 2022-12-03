
from math import sqrt

def rootSquareSolver(a = 0, b = 0, c = 0):
  
  if a == 0:
    """ Condição para que o teste e test_checkWithoutRoots seja válido """
    """ Condição para que o teste e test_checkWithoutACoefficient seja válido """
    return None
    
  if b == 0 and c != 0: 
    """ Condição para que o teste e test_checkWithoutBCoefficient seja válido """
    xsquared = -b / a
    raiz1 = -sqrt(xsquared)
    raiz2 = sqrt(xsquared)
    return [raiz1, raiz2]
    
  if b != 0 and c == 0: 
    """ Condição para que o teste e test_checkWithoutBCoefficient seja válido """
    xsquared = -b / a
    raiz1 = 0
    raiz2 = xsquared
    return [raiz1, raiz2]
  
  delta = b*b -4*a*c
  base = 2*a
  
  if delta < 0: 
    """ Condição para que o teste test_checkNegativeDelta seja válido """
    return None
    
  if delta == 0: 
    """ Condição para que o teste test_checkOneRoot seja válido """
    raiz = (-b + sqrt(delta)) / base
    return [raiz]
    
  raiz1 = (-b + sqrt(delta)) / base
  raiz2 = (-b - sqrt(delta)) / base
  return [raiz1,raiz2]