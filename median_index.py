#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Eben Pendleton"
__credits__ = "Derived from https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python"
__status__ = "Production"

def median_index(vals):
    '''
    Return the best approximate median index from a given list.
    The median index is returned if the input list has an odd number of elements
    in cases of even numbers the index closest to zero is returned

    vals: array-like and supports len
    returns median index position (zero based) following odd or even logic above
    '''

    lens = len(vals)
    # with an even number of elements pick the index closer to zero
    if lens % 2 == 0:
        index = (lens/2) -1
    else:
        # with an odd number of elements pick the median index
        index = (lens / 2)
    return index


if __name__ == '__main__':
    ''' 
    testing function that tests even, odd and float cases
    '''
    test1=[1,2,3,4,5,6]
    test2=[1,2,3,4,5,6,7]
    test3 = [0.0, 3.4, 6.7]
    tests=[test1,test2, test3]
    for t in tests:
        m_index=median_index(t)
        print(t)
        print(t[m_index])