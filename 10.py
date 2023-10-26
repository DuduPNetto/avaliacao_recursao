def calc(limit, counter=0, n=50000):
    counter += 1
    if limit == counter: return n
    return calc(limit, counter, n * 3)

print("Para exceder 200 mil bactérias são necessárias três leituras, com o total de:", calc(3), "bactérias")