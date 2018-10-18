import pytest
'''  
   Calling functions
'''

def echo(*args, **kwargs):
    """---- Example: formal and keyword arguments ----"""
    return {
        "*args=": str(args),
        "**kwargs": str(kwargs)
        }

def echoKwargsOnly(**kwargs):
    return {
        "**kwargs": str(kwargs)
    }

def test_formal_args():
    assert echo(1, 2, 3, 4) == {
        "*args=": str( (1, 2, 3, 4) ),
        "**kwargs": str( {} )
    }
        

def test_kw_args():
    assert echo(1, 2, three=3, four=4) == ""

def test_formal_kw_args():
    assert echo([1, 2, 3], {"four": 4, "five": 5}) == ""

def test_splat_args():
    assert echo(*[1, 2, 3], **{"four": 4, "five": 5}) == ""
    
def test_splat_mismatch():
    # **wont work**
    # echoKwargsOnly(*[1, 2, 3], **{"four": 4, "five": 5})
    #
    assert echoKwargsOnly(**{"four": 4, "five": 5}) == ""

def f1(arg1):
    return arg1

def f2(arg1, arg2):
    return (arg1, arg2)

def test_dict():
    """---- Example: calling arguments with an array or a dict ----"""
    assert f1(**{ 'arg1': 1 }) == ""

'''  
   Defining regular functions
'''

def info(object, spacing=10, collapse=1):
    return {
        "object": str(object),
        "spacing": str(spacing),
        "collapse": str(collapse)
    }


def test_func_name():
    assert info.__name__ == ""

'''
   Parameters
'''


def test_extra_formal_args_with_lamba():
    """ passing extra parameters to function with fixed arguments """ 
    with pytest.raises(TypeError) as exc_info:
        fixed_arg_lambda = lambda x: x*2
        fixed_arg_lambda(1,2)
    assert str(exc_info.value) == '<lambda>() takes 1 positional argument but 2 were given'

def test_extra_formal_args_with_func():
    """ passing extra parameters to lambda with fixed arguments """ 
    with pytest.raises(TypeError) as exc_info:
        def fixed_arg_func(x):
            return x*2

        fixed_arg_func(1,2)
    assert str(exc_info.value) == 'fixed_arg_func() takes 1 positional argument but 2 were given'

def test_extra_kw_args_with_lamba():
    """ passing extra parameters to function with fixed arguments """ 
    with pytest.raises(TypeError) as exc_info:
        fixed_arg_lambda = lambda x: x*2
        fixed_arg_lambda(1,y=2)
    assert str(exc_info.value) == "<lambda>() got an unexpected keyword argument 'y'"


def test_extra_mixed_args_with_lamba():
    mixed_arg_lamba = lambda x, y=None: x + y if y else x

    assert mixed_arg_lamba(1) == 1
    assert mixed_arg_lamba(1, 2) == 3
    
    
def num_args(func):
    import inspect
    if hasattr(inspect, 'getargspec'):
        return len(inspect.getargspec(func).args)
    else:
        return len(inspect.signature(func).parameters)

def test_inspect_args():
    """ test passing in the right number of parameters """
    def one_arg_func(x):
        return x

    def two_arg_func(x, y):
        return x + y

    assert num_args(one_arg_func) == 1
    assert num_args(two_arg_func) == 2
    
    
    


