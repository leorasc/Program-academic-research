from pyclbr import Function
from typing import Callable, Any

def f(x: int, y: float, z):
    return x + y + z

def concate(x, y, z):
    return x + y + z

# function taken from class summary
def error_fun(x):
    raise Exception("Invalid input", x)

def safe_call(func: Function, x: Any, y: Any, z: Any):
    """ Returns the output of func if the arguments are of the correct type of the function func.
        Otherwise, throws an exception.

    >>> safe_call(f, x=5, y=7.0, z=3)
    15.0
    >>> safe_call(f, x=5, y="abc", z=3)
    Exception: ('Invalid input', 'abc')
    >>> safe_call(concate, x="5", y="abc", z=3)
    TypeError: can only concatenate str (not "int") to str
    >>> safe_call(concate, x="5", y="abc", z="3")
    '5abc3'
    """
    annotations = func.__annotations__
    localvars = locals()
    for a in annotations.keys():
        if annotations[a] is not type(localvars[a]):
            error_fun(localvars[a])
    return func(x, y, z)

# safe_call(f, x=5, y=7.0, z=3)
# safe_call(f, x=5, y=abc, z=3)
# safe_call(string, x=5, y=abc, z=3)
# safe_call(string, x=5, y=abc, z=3)


from collections import deque

def eight_neighbor_function(node:Any)->list:
    (x,y,z) = node
    # print(node)
    return [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z),(x,y,z+1), (x,y,z-1)]


def four_neighbor_function(node:Any)->list:
    (x,y) = node
    # print(node)
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def breadth_first_search(start: Any, end: Any, neighbor_function: Callable):
    """ Returns the path from start to end, using the Callabale neighbor_function
        for moving in each step.

        >>> print(breadth_first_search(start=(0,0), end=(0,0), neighbor_function= four_neighbor_function))
        (0, 0)
        >>> print(breadth_first_search(start=(0,0), end=(1,0), neighbor_function= four_neighbor_function))
        (0, 0)(1, 0)
        >>> print(breadth_first_search(start=(0,0), end=(2,0), neighbor_function= four_neighbor_function))
        (0, 0)(1, 0)(2, 0)
        >>> print(breadth_first_search(start=(0,0), end=(2,2), neighbor_function= four_neighbor_function))
        (0, 0)(1, 0)(2, 0)(2, 1)(2, 2)

        >>> print(breadth_first_search(start=(0,0,0), end=(0,0,0), neighbor_function= eight_neighbor_function))
        (0, 0, 0)
        >>> print(breadth_first_search(start=(0,0,0), end=(1,0,0), neighbor_function= eight_neighbor_function))
        (0, 0, 0)(1, 0, 0)
        >>> print(breadth_first_search(start=(0,0,0), end=(2,0,-1), neighbor_function= eight_neighbor_function))
        (0, 0, 0)(1, 0, 0)(2, 0, 0)(2, 0, -1)
        >>> print(breadth_first_search(start=(0,0,0), end=(2,2,-2), neighbor_function= eight_neighbor_function))
        (0, 0, 0)(1, 0, 0)(2, 0, 0)(2, 1, 0)(2, 2, 0)(2, 2, -1)(2, 2, -2)
        """

    q = deque()
    visited = set()
    q.append((start, str(start)))
    # label start as explored
    visited.add(start)
    while len(q) != 0:
        v = q.popleft()
        if v[0] == end:
            return v[1]
        for w in neighbor_function(v[0]):
            if w not in visited: # w is not labled as explored
                # print(w)
                visited.add(w) #label w as explored
                q.append((w, v[1]+str(w)))



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())