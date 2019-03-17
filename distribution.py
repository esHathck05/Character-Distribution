"""
random stuff that i used and did something cool:

print(list(x*text.count(x) + str(len(list(x*text.count(x))))))

mylist = (x*len(list(x*text.count(x))))
        print(mylist)
"""
"""
distribution.py
Author: Esther Hacker
Credit: N/A

Assignment: Character Distribution
"""

text = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "' + text + '" is: ')

import string
alphabet = string.ascii_lowercase

for x in list(alphabet):
    if x in str(text):
        mylist = (x*text.count(x))
        #print(mylist)
        mylist2 = list(x + str(len(list(x*text.count(x)))))
        print(mylist2)
        #print(list(x*text.count(x) + str(len(list(x*text.count(x))))))
        
        
        
        
def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    return b > a


def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it

    
tosort = list(len(list(x*text.count(x))))
bsort(tosort, compare)
print(tosort)
