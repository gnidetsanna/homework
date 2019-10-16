#Словарь для калькулятора
import math

def add (a,b):
    res = a + b
    return res


def sub (a,b):
    res = a - b
    return res

def mul (a,b):
    res = a * b
    return res

def div (a,b):
    res = a / b
    return res

def sin(a):
    res = math.sin(a)
    return res

def cos(a):
    res = math.cos(a)
    return res

def tan(a):
    res = math.tan(a)
    return res

def cotan(a):
    res = 1/(math.tan(a))
    return res

calc_object = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'cotan': cotan
}

