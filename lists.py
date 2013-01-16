
'''  
   List data type
'''

'''
   List comprehension: [mapping−expression for element in source−list if filter−expression]
'''
# Regex pattern matching a list
# ---- Example: grep a method from module methods ----
import __builtin__
import re
methods = dir(__builtin__)
r = re.compile('call')

# Solution A:
filter(re.compile('call').search, methods)

# Solution B:
[m for m in methods if r.search(m)]
or
[m for m in methods if re.search('call', m)]

# Solution C:
l = []
for m in methods: 
  l.append(m) if r.search(m)

# Solution D:
reduce(lambda: acc, e: acc  , methods, [])

# ---- Example: getting the index list of regex matching elements within a list ----
import __builtin__
import re
methods = dir(__builtin__)
r = re.compile('call')


# ---- Example: print a list ---
l = [1, 3, "a", 3.5, [].append ]
print '[%s]' % ', '.join(map(str, l))


# ---- Example: summing/reducing the numbers ---
reduce(lambda acc,d: 10*acc+d, [1,2,3,4,5,6,7,8], 0)

# ---- Example: summing/reducing the numbers ---
l  = [True, False]
# Solution A:
reduce(lambda acc,d: acc and d, l, True)

# Solution B:
reduce(bool.__and__, l, True)
