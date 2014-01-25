'''  
   Calling functions
'''
print
print "---- Example: formal and keyword arguments ----"
print
def echo(*args, **kwargs):
    print "*args", args
    print "**kwargs", kwargs

def echoKwargsOnly(**kwargs):
    print "**kwargs", kwargs

print ">> echo(1, 2, 3, 4)"
echo(1, 2, 3, 4)

print ">> echo(1, 2, three=3, four=4)"
echo(1, 2, three=3, four=4)

print '>> echo([1, 2, 3], {"four"=4, "five"=5})'
echo([1, 2, 3], {"four": 4, "five": 5})

print '>> echo(*[1, 2, 3], **{"four": 4, "five": 5})'
echo(*[1, 2, 3], **{"four": 4, "five": 5})
# **wont work**
# echoKwargsOnly(*[1, 2, 3], **{"four": 4, "five": 5})
#
print '>> echoKwargsOnly(**{"four": 4, "five": 5})'
echoKwargsOnly(**{"four": 4, "five": 5})

print
print "---- Example: calling arguments with an array or a dict ----"
print

def f1(arg1):
    print arg1

def f2(arg1, arg2):
    print arg1, arg2

print ">>f1(**{ 'arg1': 1 })"
f1(**{ 'arg1': 1 })

'''  
   Defining regular functions
'''

def info(object, spacing=10, collapse=1):
    print "object: ", object
    print "spacing: ", spacing
    print "collapse: ", collapse


print "function name: %s" % info.__name__

'''
   Lambda functions
'''

#  Variation 1
def f1(x):
    return x*2

#  Variation 2
g = lambda x: x*2


import pdb;pdb.set_trace()

