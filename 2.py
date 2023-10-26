def progressaoGeometrica(a, r, n):
  for i in range(0, n):
    result = a * r
    print(r, "*", a, "-->", result)
    return progressaoGeometrica(result, r, n - 1)

progressaoGeometrica(1, 2, 10)