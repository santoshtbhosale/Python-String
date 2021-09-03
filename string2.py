
s = input("Enter the String:")
s1 = len(s)
s2 = 'ing'
if s2 in s:
    print(s + 'ly')
elif s1 > 3:
    print(s)
else:
    print(s + 'ing')