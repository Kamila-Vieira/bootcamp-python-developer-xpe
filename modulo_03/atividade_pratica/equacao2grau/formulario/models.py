import math
from django.db import models

class Equacao(models.Model):
  coeficienteA = models.BigIntegerField('a', null=False)
  coeficienteB = models.BigIntegerField('b', null=False)
  coeficienteC = models.BigIntegerField('c', null=False)
  resultado = models.CharField('resultado', max_length=300, null=True)
  
  def __str__(self):
    return self.calculate()
  
  def save(self, *args, **kwargs):
    self.resultado = self.calculate()
    super().save(*args, **kwargs)
  
  def calculate(self):
    if self.coeficienteA == 0 and self.coeficienteB != 0 and self.coeficienteC != 0:
      return f"Sem raízes reais"
      
    elif self.coeficienteB == 0 and self.coeficienteA!= 0 and self.coeficienteC != 0:
      xsquared = -self.coeficienteB / self.coeficienteA
      if xsquared != 0:
        raiz1 = -math.sqrt(xsquared)
        raiz2 = math.sqrt(xsquared)
        return f"Duas raízes: {raiz1} e {raiz2}"
      else:
        return f"Sem raízes reais"
    
    elif self.coeficienteC == 0 and self.coeficienteB != 0 and self.coeficienteA != 0:
      raiz1 = 0
      raiz2 = -self.coeficienteB / self.coeficienteA
      return f"Duas raízes: {raiz1} e {raiz2}"
      
    elif self.coeficienteC != 0 and self.coeficienteB != 0 and self.coeficienteA != 0:
      delta = (self.coeficienteB ** 2) - (4 * self.coeficienteA * self.coeficienteC)
      base = (2 * self.coeficienteA)
      
      if base == 0 or delta < 0:
        return f"Sem raízes reais"

      if delta == 0:
        raiz = -self.coeficienteB / base
        return f"Uma raíz: {raiz}"
      else:
        raiz1 = (-self.coeficienteB + math.sqrt(delta)) / base
        raiz2 = (-self.coeficienteB - math.sqrt(delta)) / base
        return f"Duas raízes: {raiz1} e {raiz2}"
      
    else: 
      return f"Sem raízes reais"