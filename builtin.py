import __builtin__

print '''
   Example:  builtin variables
'''
print
print '---- Example: __name__ - the current module ----'
print

print '>> __name__'
print __name__  



print
print '---- Example:  builtin functions - dir, type, etc ----'
print

print '>> dir(__builtin__)'
print dir(__builtin__)

# ---- Example: type ----
print '>> type([])'
print type([])

print '>> type([].append)'
print type([].append)

print '>> type(type)'
print type(type)

# ---- Example: help ----
# help(filter)


print '''
   Example:  function decorator
'''

print
print ' ---- Example: @property ----'
print

class Rectangle(object):
    """
    Example - test @property decorator
    """
    def __init__(self):
        self._x = None             # required. otherwise, AttributeError will be thrown when height is not initialized
    @property
    def height(self):
        print "retrieving Rectangle.height"
        return self._x
    @height.setter
    def height(self, value):
        print "setting Rectangle.height = %s" % str(value)
        self._x = value

rectangle = Rectangle()
print '>> rectangle.height = 3'
rectangle.height = 3
print '>> type(rectangle.height)'
print type(rectangle.height)

print '>> rectangle'
print rectangle        

print '>> rectangle'
print rectangle        
    
    

