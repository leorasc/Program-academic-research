from pyclbr import Function
from typing import Callable, Any
from warnings import catch_warnings

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
            catch_warnings(error_fun(localvars[a]))
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


import collections

def print_sort_set(x: set):
    s = ""
    while len(x) > 0:
        y = find_min(x)
        x.remove(y)
        if type(y) is type([]):
            s += print_sort_list(y)
        elif type(y) is type({}):
            s += print_sort_dict(y)
        elif type(y) is type(set()):
            s += print_sort_set(y)
        elif type(y) is type(tuple()):
            s += print_sort_tuple(y)
        elif type(y) is type(chr(0)):
            s += '"' + y + '"'
        else:
            s += str(y)
    return s

def find_min(x: set):
    y = x[0]
    for z in x:
        if str(z) < str(y):
            y = z
    return y

def print_sort_dict(x: dict):
    keylist = sorted(x.keys(), key = str) 
    s = "{"      
    for i in keylist:
        t = '"' if type(i) is type(chr(0)) else ""
        t = "'" if type(i) is type(str) else t
        if type(x[i]) is type([]):
            s += t + str(i) + t + ": " + print_sort_list(x[i]) + ", "
        elif type(x[i]) is type({}):
            s += t + str(i) + t + ": " + print_sort_dict(x[i]) + ", "
        elif type(x[i]) is type(set()):
            s += t + str(i) + t + ": " + print_sort_set(x[i]) + ", "
        elif type(x[i]) is type(tuple()):
            s += t + str(i) + t + ": " + print_sort_tuple(x[i]) + ", "
        elif type(x[i]) is type(chr(0)):
            s += t + str(i) + t + ': "' + str(x[i]) + '", '
        elif type(x[i]) is type(str):
            s += t + str(i) + t + ": '" + str(x[i]) + "', "
        else:
            s += t + str(i) + t + ": " + str(x[i]) + ", "
    s = s if len(s) == 1 else s[:len(s)-2] + "}"
    return s

def print_sort_tuple(x: tuple):
    return print_sort_list(sorted(x, key= str))

def print_sort_list(x: list):
    x.sort(key=str)
    s = "["
    for i in x:
        if type(i) is type([]):
            s += print_sort_list(i) + ", "
        elif type(i) is type({}):
            s += print_sort_dict(i) + ", "
        elif type(i) is type(set()):
            s += print_sort_set(i) + ", "
        elif type(i) is type(tuple()):
            s += print_sort_tuple(i) + ", "
        elif type(i) is type(chr(0)):
            s += '"' + str(i) + '"'
        elif type(i) is type(str):
            s += "'" + str(i) + "'"
        else:
            s += str(i) + ", "
    s = s if len(s) == 1 else s[:len(s)-2] + "]"
    return s

def print_sorted(x):
    """ Prints the structure of x while it is sorted
    >>> print_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]}) 
    {"a": 5, "b": [1, 2, 3, 4], "c": 6}
    >>> print_sorted({"z": 5, "d": 6, "b": [1, 3, 2, 4]})
    {"b": [1, 2, 3, 4], "d": 6, "z": 5}
    >>> print_sorted({"x": 5, "c": 6, "a": [6, 3, 2, 4]})
    {"a": [2, 3, 4, 6], "c": 6, "x": 5}
    """

    s = ""
    if type(x) is type([]):
        s += print_sort_list(x)
    elif type(x) is type({}):
        s += print_sort_dict(x)
    elif type(x) is type(set()):
        s += print_sort_set(x)
    elif type(x) is type(tuple()):
        s += print_sort_tuple(x)
    elif type(x) is type(chr(0)):
        s += '"' + str(x) + '"'
    elif type(x) is type(str):
        s += "'" + str(x) + "'"
    else:
        s += str(x)
    print(s)



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())