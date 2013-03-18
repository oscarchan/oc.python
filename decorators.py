print """
   decorator with class
"""

class logging_decorator(object):
    def __init__(self, arg1, *args, **kwargs):
        print "logging_decorator.__init__(arg1=%s, *args=%s, **kwargs=%s)" % (arg1, args, kwargs)
        self.arg1 = arg1
        self.args = args
        self.kwargs = kwargs
    def __call__(self, arg1, *args, **kwargs):
        print "logging_decorator.__call__(arg1=%s, *args=%s, **kwargs=%s)" % (arg1, args, kwargs)

class decorator_with_noargs(object):
    def __init__(self, wrapped): 
        print "decorator_with_noargs.__init__(wrapped=%s)" % (wrapped)
        self.wrapped = wrapped
    def __call__(self, *args, **kwargs):
        print "decorator_with_noargs.__init__(*args=%s, **kwargs=%s)" % (args, kwargs)
        returned = self.wrapped(*args, **kwargs)
        print "decorator_with_noargs.__init__: ends"
        return returned

class decorator_with_args(object):
    def __init__(self, filter_parameters = []):
        print "decorator_with_args.__init__(filter_parameters=%s)" % (filter_parameters)
        self.filter_parameters = filter_parameters
    def __call__(self, wrapped):
        print "decorator_with_args.__call__(wrapped=%s)" % (wrapped)
        
        def wrap(*args, **kwargs):
            print "decorator_with_args.__call__.wrap(*args=%s, **kwargs=%s)" % (args, kwargs)
            returned = wrapped(*args, **kwargs)
            print "decorator_with_args.__call__.wrap: ends"

            return returned

        return wrap

def decorator_with_optional_args(*args, **kwargs):
    def wrapper(func):
        def _func(*args, **kwargs):
            print "decorator_with_optional_args._func(*args=%s, **kwargs=%s)" % (args, kwargs)
            returned = func(*args, **kwargs)
            print "decorator_with_optional_args._func: ends"
            return returned
        return _func

    if len(args) == 1 and callable(args[0]):
        # no arguments, this is the decorator
        return wrapper(args[0])
    else:
        return wrapper





print "---- Example: function decorator class without arguments ----"
@logging_decorator
def f1(user, password):
    return "f1"


@decorator_with_noargs
def f1a(user, password):
    return "f1a"


print "f1 returned=", f1(13423, "abcd"), "<< None is expected"
print "f1a returned=", f1a(13423, "abcd"), "<<"

        

print "---- Example: function decorator class with arguments ----"
print """
  @logging_decorator({"filtered": ["password", "auth_cookie"]})
  def f2(user, password):
"""
@logging_decorator({"filtered": ["password", "auth_cookie"]})
def f2(user, password):
    '''
    f2 can't be called!!
    '''
    print "f2"

print """
   @decorator_with_args(filter_parameters=["abc"])
   def f2a(user, password):
"""
@decorator_with_args(filter_parameters=["abc"])
def f2a(user, password):
    print "f2a"

print "f2a returned=", str(f2a(13423, "abcd")), "<<"


print "---- Example: function decorator class with optional arguments ----"


print """
@decorator_with_optional_args
def f3a(user, password):
"""
@decorator_with_optional_args
def f3a(user, password):
    print "f3a"
    return "f3a"

print "f3a returned=", f3a(13423, "abcd"), "<<"

print """
@decorator_with_optional_args(test="testme")
def f3b(user, password):
    print "f3b"
    return "f3b"
"""
@decorator_with_optional_args(test="testme")
def f3b(user, password):
    print "f3b"
    return "f3b"

print "f3b returned=", f3b(13423, "abcd"), "<<"


# --- Example: functools.wraps ---
from functools import wraps

def component_status(wrapped):
    print "component_status.wrapping %s" % wrapped
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        print 'component_status.wrapper: args=%s, kwargs=%s' % args, kwargs
        return wrapped(*args, **kwargs)
    return wrapper

@component_status
def get_db_status():
    return "db.status"


