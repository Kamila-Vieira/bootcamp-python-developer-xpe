def remove_par(lista):
  for numero in lista:
    if numero % 2 == 0: 
      lista.remove(numero)
  return lista
  
# Encontra e retorna o maior número impar presente na lista
def maior_impar(lista):
  # Lista com valores pares removidos
  lista_impares = remove_par(lista)
  # Retorna o maior número da lista
  maior_numero = max(lista_impares)
  return maior_numero
 
# Encontra e retorna o menor número impar presente na lista
def menor_impar(lista):
  # Lista com valores pares removidos
  lista_impares = remove_par(lista)
  # Retorna o menor número da lista
  menor_numero = min(lista_impares)
  return menor_numero
 
# Encontra e retorna o maior e o menor número impar presentes na lista
def maior_menor_impar(lista):
  # Lista com valores impares removidos
  lista_impares = remove_par(lista)
  # Retorna o maior e o menor número da lista
  maior_numero = max(lista_impares)
  menor_numero = min(lista_impares)
  return (maior_numero, menor_numero)