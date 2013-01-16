class  view_config:
    def __init__(self):
        print "view_config.__init__"
    def __call__(self, wrapped):
        print "view_config.__call__"
        return wrapped

# -- wouldn't figure out how to make it work --
@view_config
def f2(arg1, arg2):
    print "f2"


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


