
class ParentClass:
    __member_var_1 = []   #!!!!!!!! bad idea !!!!!!! -- the variable is ONLY initiate ONCE for all variables

class ChildClass(ParentClass):
    "showing the child-parent relationship"
    def __init__(self):
        pass


# --- Example: print the class hierarchy ----

# Solution 1 - class.__bases__
def printClassInfo(clazz):
    print "Class: %s" % clazz.__name__
    print "Parent: %s" %  ", ".join([clazz.__name__ for c in clazz.__bases__ ])
    print "methods: %s" % ", ".join([clazz]  )

# Solution 2 - inspect.getclasstree([..])
import inspect
inspect.getclasstree([ValueError])

''' Special class methods
    def __getitem__(self, key)
    def __setitem__(self, key, value)
    def __repr__(self): return repr(self.data)
    def __cmp__(self, dict):
        if isinstance(dict, UserDict):
            return cmp(self.data, dict.data)
        else:
            return cmp(self.data, dict)
    def __len__(self): return len(self.data)
    def __delitem__(self, key): del self.data[key]
'''

class ChildClass(ParentClass):
    def __getitem__(self, key):
        return 1 #  ("child class item: key=%s" %s key)
    def __setitem__(self, key, value): 
        1 + 1
        
class ChildClass(ParentClass):
    def __repr__(self): return "ChildClass"*

# ---- Example: access dict as property ----
from helpers import dot_dict

payload = {
  "service_name" : "authsvc",
  "components" : {
    "db_account" : {
      "status" : "up"
    },
    "cache.redis" : {
      "status" : "up"
    }
  },
  "service_version" : "0.0.13-master",
  "component_keys" : [
    "db_account",
    "cache.redis"
  ],
  "pid" : 6423
}        

body = dot_dict(payload)
print body.service_name
print body.components.get('db_account').status
body.components.db_account.status = 'down'

'''
   class attributes
'''
# ---- Example:  ---
class ClassAttribute:
    """
    Class Attribute is to test __dict__ variable
    """
    attr1 = "some random string"

print "same __doc__" if ClassAttribute.__doc__ == ClassAttribute.__dict__['__doc__'] else "different __doc__"
print "same attr1" if ClassAttribute.attr1 == ClassAttribute.__dict__['attr1'] else "different attr1"



