# a
def Sa(limit, counter=0, n=1):
    if limit == 1: return 1
    if counter == limit - 1: return n
    return Sa(limit, counter + 1, n * 3)
print(Sa(4))

# b
def Sb(limit, counter=0, n=2):
    if limit == 1: return 2
    if counter == limit - 1: return n
    return Sb(limit, counter + 1, n / 2)
print(Sb(4))

# c
def Sc(limit, counter=0, numbers=[0, 0]):
    counter += 1
    if limit == 1: 
        numbers[0] += 1 
    elif limit == 2:
        numbers[1] += 1
    elif counter % 2 == 1 and counter != 1:
        numbers[0] += 1
        numbers[1] += 1
    elif counter % 2 == 0 and counter != 0 and counter != 2:
        numbers[1] += 1
    if counter == limit:
        if numbers[0] == 0: return 'b'
        if numbers[0] == 1 and numbers[1] == 0: return 'a'
        if numbers[0] == 1 and numbers[1] == 1: return 'a + b'
        if numbers[0] == 1 and numbers[1] > 1: return 'a + ' + str(numbers[1]) + 'b'
        return str(numbers[0]) + 'a + ' + str(numbers[1]) + 'b'
    return Sc(limit, counter, numbers)
print(Sc(5))

# d
def Sd(limit, counter=0, numbers=['+', 0]):
    counter += 1
    if counter % 2 == 1:
        numbers[0] = '+'
    elif counter % 2 == 0:
        numbers[0] = '-'
        numbers[1] += 1
    if counter == limit:
        if limit == 1: return 'p'
        if numbers[1] == 1: return 'p ' + numbers[0] + ' q'
        return 'p ' + numbers[0] + ' ' + str(numbers[1]) + 'q'
    return Sd(limit, counter, numbers)
print(Sd(5))