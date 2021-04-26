import pytest

# Here are some example functions to run, can of course be replaced by your own to test things out
def turtle(n=1000000):
    """Regular for loops"""
    x = [] 
    for i in range(n,0,-1):
        x.append(str(i))

    s= ""
    for i in x:
        s+= i

def cheetah(n=1000000):
    """Faster with list comprehenssion and join"""
    x = [str(i) for i in range(n,0,-1)]
    s = "".join(x)

# This is where pytest gets called   
def test_case(benchmark):
    benchmark(turtle)