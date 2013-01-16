

'''   If condition expression
 if (A if C else B):
    [x for x in seq if (A if C else B)]
    A if (X if C else Y) else B
    (A if C else B) if D else E
'''

first = "first"
second = "second"
condition = True

x =  first if condition else second
print x   # output: first

condition = False
x =  first if condition else second
print x   # output: second


x = A if C else B
x = lambda: A if C else B
x = A if C else B if D else E


''' loop expression
'''

for item in list
