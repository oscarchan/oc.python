class dot_dict:
    '''
    access a dictionary via dot notation
    '''
    def __init__(self, wrapped_dict):
        self.__dict__['map'] = wrapped_dict
    def get(self, name):
        return self.__getattr__(name)
    def __getattr__(self, name):
        value = self.__dict__['map'].get(name)
        if type(value) is dict:
            value = dot_dict(value)
        return value
    def __setattr__(self, name, value):
        self.__dict__['map'].update([[name, value]])
    def __repr__(self):
        return repr(self.__dict__['map'])

