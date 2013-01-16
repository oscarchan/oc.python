import inspect

def printClassInfo(obj):
    print ">>> type: ", type(obj)
    print obj.__class__, ": base classes: ", obj.__class__.__bases__
    print inspect.getclasstree([type(obj)])

class HelloMixin(object):
    def hello(self):
        print "%s.hello" % self.__class__.__name__

class Hello2Mixin(object):
    def hello(self):
        print "%s.hello2" % self.__class__.__name__

class PingMixin(object):
    def ping(self):
        print "%s.hello2" % self.__class__.__name__

print
print "---- Example: Test simple mixin case ----"
print
class BasicMixinExample(HelloMixin): pass

example = BasicMixinExample()
example.hello()
printClassInfo(example)

print
print "---- Example: Test 2-mixin class ----"
print

class Mix2Example(HelloMixin, PingMixin): pass
example = Mix2Example()
printClassInfo(example)

print
print "---- Example: Test conflict resolution of Mixins ----"
print

class Conflict1Example(HelloMixin, Hello2Mixin): pass
class Conflict2Example(Hello2Mixin, HelloMixin): pass

"""
   methods are called from left to right in the inheritance
"""
example1 = Conflict1Example()
example2 = Conflict2Example()

print "HelloMixin First: ", example1.hello()
print "Hello2Mixin First: ", example2.hello()

printClassInfo(example1)
printClassInfo(example2)

print
print "---- Example: Test conflict resolution of Mixins in the deep of inheritance tree ----"
print

class DeepConflict1Example(Conflict1Example, Hello2Mixin): pass
class DeepConflict2Example(Conflict2Example, HelloMixin): pass

example1 = DeepConflict1Example()
example2 = DeepConflict2Example()

print
print "---- Example: Test conflict resolution of Mixins in the deep of inheritance tree ----"
print

"""
   methods are called from deep first
"""

print "Deep HelloMixin First: ", example1.hello()
print "Deep Hello2Mixin First: ", example2.hello()

printClassInfo(example1)
printClassInfo(example2)

