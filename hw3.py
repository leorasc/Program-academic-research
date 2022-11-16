import re

def print_emails(sfile):
    """ Prints the valid emails in a list, and then the not valid ones.
    >>> print_emails("hw-week3//emails.txt")
    valid:
    abc_def@mail.com
    aa@ma-il.cc
    a.a_xc-ks@mail.cc
    a@mail.cc
    aa@mail.cc
    abc-d@mail.com
    Leorabach@gmail.com
    Leorab.ach@gmail.com
    not valid:
    _aa@mail.cc
    abc-@mail.com
    abc..def@mail.com
    Leorabach@gmail.c
    .abc@mail.com
    abc#def@mail.com
    L$e%o@r#abach@gmail.com
    """
    with open(sfile, 'r') as file:
        s = file.read()
        lst = [s.split(" ")]
        valid = []
        n_valid = []
        for l in lst:
            for s in l:
                query = re.match(r"[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*[.][a-zA-Z0-9]{2,}\b", s, flags=0)
                if query is not None:
                    valid.append(query.group())
                else:
                    query = re.match(r"\S*",s,flags=0)
                    if query.group() != '':
                        n_valid.append(query.group())

    print("valid:")
    for s in valid:
        print(s)

    print("not valid:")
    for s in n_valid:
        print(s)

import math
from pyclbr import Function
from typing import Any

def lastcall(func: Function):
    """
    The decorator returns the function with its answer, if it wasn't called with that parameter yet.
    Otherwise, it prints a message that it already was called.
    >>> print_type("S")
    S is a 'str'
    >>> print_type("S")
    I already told you that the answer is None!
    >>> print(pow2(2))
    4
    >>> pow2(2)
    I already told you that the answer is 4!
    >>> print_type(2)
    2 is a 'int'
    >>> print(pow2(10))
    100
    >>> pow2(2)
    I already told you that the answer is 4!
    >>> pow2(10)
    I already told you that the answer is 100!
    
    """
    dic = {} # An empty dictionary for checking if the parameter and the function were called already.
    def wrapper(x):
        if (x,func) in dic.keys():
            print("I already told you that the answer is "+str(dic[(x,func)])+"!")
        else:
            dic[(x,func)]= func(x)
            return dic[(x,func)]
    return wrapper

@lastcall
def pow2(x: float):
    return x**2

@lastcall
def powx(x: float):
    return x**x

@lastcall
def print_type(x: Any):
    s = str(type(x))
    print(str(x) + " is a " + s[7:len(s)-1])

@lastcall
def loge(x: int):
    return math.log(x)

@lastcall
def log2(x: int):
    return math.log2(x)

@lastcall
def log10(x: int):
    return math.log10(x)

# print_emails("hw-week3//emails.txt")
# print_type("S")
# print_type("S")
# print(pow2(2))
# pow2(2)
# print_type(2)
# print(pow2(10))
# pow2(2)
# pow2(10)



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
