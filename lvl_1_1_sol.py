def answer(data, n):
    anArray = data
    countCheck = {}
    for index, item in enumerate(data):
        countCheck[item] = countCheck.setdefault(item, 0) + 1
        if (index == 99):
            break

    for key, value in countCheck.iteritems():
        if (value > n):
            anArray = filter(lambda toRemove: toRemove != key, anArray)
    return anArray

print answer([2, 8, 9, 1, 4, 8, 4, 8], 2)
