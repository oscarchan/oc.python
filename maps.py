'''
   Map comprehension: 
   In python 2,
      dict((k, v) for (k, v) in map.items())
'''

# List to a map


'''
   Regex pattern matching a list
'''
print
print " ---- Example: grep a method from module methods ---- "
print 

import __builtin__
import re
methods = dir(__builtin__)
r = re.compile('call')

# Solution A:
print ">> filter(r.search, methods)"
print filter(r.search, methods)

# Solution B:
print ">> [m for m in methods if r.search(m)]"
print [m for m in methods if r.search(m)]

print ">> [m for m in methods if re.search('call', m)] "
print [m for m in methods if re.search('call', m)]

# Solution C:
l = []
for m in methods:
   if r.search(m):
     l.append(m)

print """
>> l = []
>> for m in methods: 
>>  l.append(m) if r.search(m)
"""
print l

# Solution D:
print "reduce(lambda: acc, e: acc  , methods, [])"
#print reduce(lambda: acc, e: acc, methods, [])


print
print " ---- Example: getting the index list of regex matching elements within a list ---- "
print

import __builtin__
import re
methods = dir(__builtin__)
r = re.compile('call')


print 
print " ---- Example: print a list --- "
print 
l = [1, 3, "a", 3.5, [].append ]
print '[%s]' % ', '.join(map(str, l))



print 
print " ---- Example: performance of dict constructor vs dict literal ---- "
print 

from timeit import timeit 

times = 100000

def print_timeit(stmt, times):
  print stmt
  print "\t --> took ", timeit(stmt, number=times), " sec(s)"


print_timeit("{}", times)
print_timeit("dict()", times)
print_timeit("{'a':1, 'b':2}", times)
print_timeit("dict(a=1, b=2)", times)
print_timeit("""
{
  'a':1, 'b':2,
  'c':3, 'd':4,
  'e':5, 'f':6
}""", times)
print_timeit("""
dict(
  a=1, b=2,
  c=3, d=4,
  e=5, f=6
)""", times)


