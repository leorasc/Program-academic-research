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


class List(list):
    def __init__(self, lst):
        self.lists = []
        self.len = 0
        for i in range(len(lst)):
            if type(lst[i]) == list:
                self.lists.append(List(lst[i]))
            else:
                self.lists.append(lst[i])

    def __setitem__(self, *arg, value: object):
        print("setitem")
        if len(arg) == 1:
            self.lists[arg] = value
        else:
            self.lists[arg[0]][arg[1:]] = value

    def __getitem__(self, *arg):
        if len(arg[0]) == 1:
            return self.lists[arg[0][0]]
        else:
            return self.lists[arg[0][0]][arg[0][1:]]

    def __str__(self):
        s = ""
        for i in range(len(self.lists)):
            s += str(self.lists[i])
        return s

    def __repr__(self):
        s = ""
        for i in range(len(self.lists)):
            s += str(self.lists[i])
        return s

    def __len__(self):
        return self.len

# from typing import Type
# list = Type(List)


mylist = List([[[1,2,3,33],[4,5,6,66]], [[7,8,9,99],[10,11,12,122]], [[13,14,15,155],[16,17,18,188]], ] ) 
print(mylist[0,1,3])
# print(mylist[0])
# [[1,2,3,33],[4,5,6,66]]



# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
