factorVals = [1, 11, 1, -4, 1, 1, 0]


def max5Factors(factorVals):
    listMax = []
    factors = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    factorVals2 = factorVals.copy()
    factors2 = factors.copy()
    for i in range(5):
        valueMax = max(factorVals)
        indices = []
        for j in range(len(factorVals)):
            if factorVals[j] == valueMax:
                indices.append(j)
                listMax.append([factors[j], factorVals[j]])
        print(indices)
        factorVals = [element for i, element in enumerate(factorVals) if i not in indices]
        factors = [element for i, element in enumerate(factors) if i not in indices]
        if len(listMax) == 5 or len(listMax) > 5:
            break
    listMin = []
    print(factorVals2)
    for i in range(5):
        valueMin = min(factorVals2)
        indices = []
        for j in range(len(factorVals2)):
            if factorVals2[j] == valueMin:
                indices.append(j)
                listMin.append([factors2[j], factorVals2[j]])
        print(indices)
        factorVals2 = [element for i, element in enumerate(factorVals2) if i not in indices]
        factors2 = [element for i, element in enumerate(factors2) if i not in indices]
        if len(listMin) == 5 or len(listMin) > 5:
            break
    return listMax, listMin



print(max5Factors(factorVals))