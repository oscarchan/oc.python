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
    def __init__(self, *args, **kwargs):
        print "decorator_with_args.__init__(*args=%s, **kwargs=%s)" % (args, kwargs)
        self.args = args
        self.kwargs = kwargs
    def __call__(self, wrapped):
        print "decorator_with_args.__call__(wrapped=%s)" % (wrapped)
        
        def wrap(*args, **kwargs):
            print "decorator_with_args.__call__.wrap(*args=%s, **kwargs=%s)" % (args, kwargs)
            returned = wrapped(*args, **kwargs)
            print "decorator_with_args.__call__.wrap: ends"

            return returned

        return wrap

    



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
@logging_decorator({"filtered": ["password", "auth_cookie"]})
def f2(user, password):
    print "f2"

f1(13423, "abcd")

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


