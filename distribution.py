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
print(list(alphabet))

def check_freq(str):
    freq = {}
    for c in str:
       freq[c] = str.count(c)
    return freq

numberofletters = check_freq(text)
print(numberofletters)