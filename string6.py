"""
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""
s = 'google.com'

d = {}
for i in s:
    key = d.keys()
    if i in key:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)