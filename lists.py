# -*- coding: utf-8 -*-
import string
import random
from operator import itemgetter, attrgetter
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
# or
[m for m in methods if re.search('call', m)]

# Solution C:
l = []
for m in methods: 
  if r.search(m):
    l.append(m) 

# Solution D:
reduce(lambda acc, e: acc  , methods, [])

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


print " ---- Example: soring a string list ---- "
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(size))

values = [ id_generator() for _ in xrange(10) ]
print ">>> values = %s " % str(values)

print ">>> sorted(values, key=str.lower) "
print sorted(values, key=str.lower)

print ">>> sorted(values, key=str.lower, reverse=True) "
print sorted(values, key=str.lower, reverse=True)


print " ---- Example: soring a list of object ---- "

def object_generator():
    return dict(
      id=id_generator(size=6),
      username=id_generator(size=10),
      email=id_generator() + '@test.com'
      )

values = [ object_generator() for _ in xrange(10) ]
print ">>> values = %s " % str(values)

# no particular order - on mac, it seems to be related to 
#print ">>> sorted(values) "
#print sorted(values)

print ">>> sorted(values, key=lambda item: item['id'])"
print sorted(values, key=lambda item: item['id'])


print ">>> sorted(values, key=lambda item: item['id'], reverse=True)"
print sorted(values, key=lambda item: item['id'], reverse=True)

