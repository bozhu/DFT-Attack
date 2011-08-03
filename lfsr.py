#/usr/bin/env sage

from sage.all import *

def lfsr(polynomial, init_value, field = GF(2), length = None):
    """"
    polynomial can be polynomial in GF with list() -- [c0, c1, ...]
    or a list with corresponding coefficients
    """
    coeffs = list(polynomial)[:-1] # remove the last element
    states = list(init_value)
    assert len(states) == len(coeffs)
    if None == length:
        length = field.order() ** len(states) - 1

    for i in xrange(length):
        feedback = field(0)
        for j, ele in enumerate(coeffs):
            if ele != 0: 
                feedback += states[j]

        states.append(feedback)
        yield states.pop(0)



if __name__ == '__main__':
    f = [1, 0, 0, 0, 1, 1, 1]
    s = [0, 0, 1, 0, 0, 0]

    generator = lfsr(f, s)
    for i in generator:
        print i,
