#!/usr/bin/python3
""" Find_peak: function that find peak"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak
    Returns: peak of list_of_integers[index] or None
    """
    sizeArr = len(list_of_integers) - 1
    index = 0
    middle = sizeArr
    if sizeArr == -1:
        return None
    while (index < sizeArr):
        middle = (index + sizeArr) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            index = middle + 1
        else:
            sizeArr = middle
    return list_of_integers[index]

