import types

print '''
  monkey patching
'''
def foo():
    pass

class A(object):
    def bar(self):
        pass

a = A()
a.foo = types.MethodType(foo, a)


print "function type: ", type(foo), foo
print "class member method type from class (unbound): ", type(A.bar), A.bar
print "instance method type (bound): ",   type(a.bar), a.bar
print "patched instance method type (bound): ", type(a.foo), a.foo

print '''
  duck typing
'''

class B(object):
    def bar(self):
        pass


b = B()

if hasattr(b, 'bar'):
    print "bar() exists"
