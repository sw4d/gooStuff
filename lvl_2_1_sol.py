def answer(l):
    from itertools import permutations
    option = 0

    for L in reversed(range(0, len(l) + 1)):
        if len(str(option)) > L: break # this part isn't updating til the loop breaks
        for subset in set(permutations(l, L)):
            sub = list(reversed(subset))
            if reduce(lambda x, y: (x * 10 + y) % 3, sub) == 0:
                local = reduce(lambda x, y: x * 10 + y, sub)
                if local > option:
                    option = local
    return option
print answer([3, 1, 4, 1, 5, 9])
