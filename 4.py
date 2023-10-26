lista = [6, 9, 16, 21, 26, 54, 72, 218]

def pertenceT(menor, num, num2, n):
  num3 = num * num2

  if n == num or n == num2 or n == num3:
    return True

  if menor:
    if num3 > n:
      return False
    if pertenceT(menor, num, num3, n):
      return True
    if pertenceT(menor, num2, num3, n):
      return True
  return False

for i in lista:
  print(pertenceT(True, 2, 3, i))