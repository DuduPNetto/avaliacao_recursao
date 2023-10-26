def triangle(limit, n=0, counter=1):
    if limit == 1: return 1
    if counter == limit: return n + 1
    counter += 1
    n += counter
    return triangle(limit, n, counter)

print(triangle(4))