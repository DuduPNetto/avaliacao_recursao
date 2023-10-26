def Rotina (L, j, m):
  if (j == 1):
    print(f'Maior: {m}')
    return L
  print(L[j])
  
  return Rotina (L, j - 1, m);

if __name__ == '__main__':
  inicial = 4
  L = [3, 7, 4, 2, 6 ] 
  Rotina(L, inicial, L[inicial])