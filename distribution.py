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
        print(list(x*text.count(x) + str(len(list(x*text.count(x))))))
        """
        mylist = ''.join(list(x*text.count(x) + str(len(list(x*text.count(x)))))[-1])
        print(mylist)
        """