"""
Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'
"""
s1 = 'restart'
s2 = s1[0]
s1 = s1.replace('r', '$')
s1 = s2 + s1[1:]
print(s1)