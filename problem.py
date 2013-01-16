import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)

def loggable(f):
    @wraps(f)
    def log_func(*args, **kwargs):

        start = time.time()
        try: 
            returned = f(*args, **kwargs)
        except Exception, e:
            returned = e
            raise
        else:
            return returned
        finally:
            end = time.time()
            total_time = end - start
            
            logger.info("!! %s" % str(args))
            logger.info(kwargs)
            logger.info( "--", f.__name__)
            logger.info("1: %s" % str(returned))
            logger.info("1: %s" % str(total_time))
            
    return log_func

MAP = '_map'
class dottable(object):
    '''
    a adapter for access a dictionary via dot notation

    '''
    def __init__(self, wrapped_dict = None):
        self.__dict__[MAP] = wrapped_dict if wrapped_dict else dict()
    def get(self, name):
        return self.__getattr__(name)
    def __getattr__(self, name):
        print "__getattr__ %s" % name, self.__dict__[MAP]
        value = self.__dict__[MAP].get(name)
        if type(value) is dict:
            value = dot_dict(value)
        print "%s ---> %s " % (name, value)

        return value
    def __setattr__(self, name, value):
        self.__dict__[MAP].update([[name, value]])
    def as_dict(self):
        return self.__dict__[MAP]
    # def __repr__(self):
    #     return repr(self.__dict__[MAP])
    def __str__(self):
        return str(self.__dict__[MAP])


sample = {
    "a": 1,
    "b": 2
}

@loggable
def printInfo(a, b, c):
    print a, b, c


dsample = dottable(sample)

print "__dict__",  dsample.__dict__
printInfo(1, 2, dsample)
