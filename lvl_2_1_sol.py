def answer(l):
    from itertools import permutations
    option = 0
    #We reverse so we can start with the largest index number first instead of the usual inital index of 0.
    #This is important since our goal is to find the largest number possible and quickly.
    for L in reversed(range(0, len(l) + 1)):
        #Permutations will iterate through our inital array submitted (l) with whichever index value we're on (L)
        #set is used to prevent us from having to iterate over duplicate permutations for arrays with duplicate values
        #   IE [3,1,3] => permutations will spit out duplicate data when iterating through 3.
        #       vs.
        #      [1,2,3] => data will be different each iteration since no array values are the same.
        for subset in set(permutations(l, L)):
            sub = list(reversed(subset))
            if reduce(lambda x, y: (x * 10 + y) % 3, sub) == 0:
                local = reduce(lambda x, y: x * 10 + y, sub)
                if local > option:
                    option = local
    return option
print answer([3, 1, 4, 1, 5, 9])
