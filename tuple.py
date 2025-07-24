def fun():
    a = [1, 2, 3, 3, 4] #list
    a1 = []
    a2 = [5]
    '''
    Ordered, so we can index  0 to n
    Indexed
    Allow Duplicate
    Allows Heterogenios data
    Mutable
    '''
    b = (4, 5, 6, 7) #tuple
    b1 = ()
    b2 = (5, )
    b3 = (5)
    '''
    Ordered, so we can index  0 to n
    Indexed
    Allow Duplicate
    Allows Heterogenios data
    Not Mutable
    '''
    c = {2, 4, 6} # Set
    c1 = {} # wrong
    c1 = set()

    '''
    Unordered, so we can index  0 to n
    No Indexed
    Automatically removes Duplicate
    Allows Heterogenios data
    '''