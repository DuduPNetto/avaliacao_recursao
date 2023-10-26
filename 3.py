lista = [6, 7, 19, 12]

def pertenceT(menor, num, n):
  num2 = num * 2
  num3 = num + 3

  if n == num or n == num2 or n == num3:
    return True

  if menor:
    if num > n:
      return False
    if pertenceT(menor, num2, n):
      return True
    if pertenceT(menor, num3, n):
      return True
  return False

for i in lista:
  print(pertenceT(True, 2, i))