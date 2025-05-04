##***** This was submitted

"""
def fibonacciModified(t1, t2, n):
    sys.set_int_max_str_digits(10**6) 
    for _ in range(1, n):
        t1, t2 = t2, t1 + pow(t2, 2)
    return t1
"""

#************************88

"""
import sys
sys.set_int_max_str_digits(10000000)

def fibonacciModified(t1, t2, n):
    for _ in range(n - 2):
        t3 = t1+t2**2
        t1 = t2
        t2 = t3
    return t3
"""