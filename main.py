def func(i):
    """
        >>> func(1)
        1
    """    
    if i % 15 == 0:
        print "fizzbuzz"
    elif i % 3 == 0:
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    for i in range(16):
        func(i)
