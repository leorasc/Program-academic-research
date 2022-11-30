import itertools as it


def bounded_subsets(lst: list, s: float):
    """
    Returns subsets that their sum is not larger than the given parameter s.
    They are returnd according to amonut of elements.
    >>> [s for s in zip(range(5), bounded_subsets(range(100), 1000000000000))]
    [(0, ()), (1, (0,)), (2, (1,)), (3, (2,)), (4, (3,))]
    >>> [s for s in bounded_subsets([1,2,3], 4)]
    [(), (1,), (2,), (3,), (1, 2), (1, 3)]
    >>> [s for s in bounded_subsets(range(50,150), 103)]
    [(), (50,), (51,), (52,), (53,), (54,), (55,), (56,), (57,), (58,), (59,), (60,), (61,), (62,), (63,), (64,), (65,), (66,), (67,), (68,), (69,), (70,), (71,), (72,), (73,), (74,), (75,), (76,), (77,), (78,), (79,), (80,), (81,), (82,), (83,), (84,), (85,), (86,), (87,), (88,), (89,), (90,), (91,), (92,), (93,), (94,), (95,), (96,), (97,), (98,), (99,), (100,), (101,), (102,), (103,), (50, 51), (50, 52), (50, 53), (51, 52)]
    """
    if lst is list:
        lst.sort()
    for l in range(len(lst)):
        if s < sum(lst[:l]):
            break
        for t in it.combinations(lst,l):
            if s >= sum(t) :
                yield t
    


def sorted_bounded_subsets(lst: list, s: float):
    """
    Returns subsets that their sum is not larger than the given parameter s.
    They are returnd according to their sum.    
    >>> [s for s in zip(range(5), sorted_bounded_subsets(range(100), 1000000000000))]
    [(0, ()), (1, (0,)), (2, (1,)), (3, (0, 1)), (4, (2,))]
    >>> [s for s in sorted_bounded_subsets([1,2,3], 4)]
    [(), (1,), (2,), (3,), (1, 2), (1, 3)]
    >>> [s for s in sorted_bounded_subsets(range(50,150), 103)]
    [(), (50,), (51,), (52,), (53,), (54,), (55,), (56,), (57,), (58,), (59,), (60,), (61,), (62,), (63,), (64,), (65,), (66,), (67,), (68,), (69,), (70,), (71,), (72,), (73,), (74,), (75,), (76,), (77,), (78,), (79,), (80,), (81,), (82,), (83,), (84,), (85,), (86,), (87,), (88,), (89,), (90,), (91,), (92,), (93,), (94,), (95,), (96,), (97,), (98,), (99,), (100,), (101,), (50, 51), (102,), (50, 52), (103,), (50, 53), (51, 52)]
    """
    yield ()
    if lst is list:
        lst.sort()
    for i in range(lst[0],min(sum(lst)+1,s+1)): # makes sure that the bounded subsets are ordered according to thier sum.
        for l in range(1,len(lst)):
            if i < sum(lst[:l]):
                break
            for t in it.combinations(lst,l):
                if i == sum(t) :
                    yield t
    



if __name__ == "__main__":
    import doctest

    print(doctest.testmod())





