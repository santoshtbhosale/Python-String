"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
s = 'abc'
s1 = 'xyz'
a = s1[:2] + s[2]
b = s[:2] + s1[2]
print(a, "", b)