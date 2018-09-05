import pytest
import functools

def add(value, increment):
    return increment + value

def multi(value, factor):
    return value * factor

def div(divider, value):
    return value / divider

add_1 = functools.partial(add, increment=1)
add_2 = functools.partial(add, increment=2)
add_3 = functools.partial(add, increment=3)
add_4 = functools.partial(add, increment=4)

multi_2 = functools.partial(multi, factor=2)
multi_3 = functools.partial(multi, factor=3)
multi_5 = functools.partial(multi, factor=5)

div_by_2 = functools.partial(div, 2)

def test_partial():
    assert add(1, 2)== 3
    assert add_1(2) == 3
    assert add_2(3) == 5
    assert add_3(4) == 7
    assert multi_2(3) == 6
    assert multi_3(5) == 15
    assert multi_5(7) == 35
    assert div_by_2(6) == 3
    assert div_by_2(8) == 4

    with pytest.raises(TypeError) as exc_info:
        #
        broken_func = functools.partial(add, factor=2)
        broken_func(1)

    assert "add() got an unexpected keyword argument 'factor'" in str(exc_info.value)

def test_reduce():
    """
    reduce(func, iterable[, init_val)
    func = lambda(acc, item)

    :return:
    """
    pass


def test_simple_chain_handler():
    funcs = [add_1, multi_3, add_2, multi_5, add_3, multi_2, add_4]
    sample2 = [2, 3, 5, 7, 11, 13]
    expected_output_func = lambda a: (((((((s + 1) * 3) + 2) * 5) + 3 ) * 2) + 4)

    def chain_func(acc, f):
        return f(acc)

    chain_func2 = lambda acc, f: f(acc)

    for s in sample2:
        assert functools.reduce(chain_func, funcs, s) == expected_output_func(s)

    for s in sample2:
        assert functools.reduce(chain_func2, funcs, s) == expected_output_func(s)

    chained_handler = simple_chained_handler(funcs)

    for s in sample2:
        assert chained_handler(s) == expected_output_func(s)

def simple_chained_handler(handlers):
    def chained_handler(init_value):
        value = init_value
        for handler in handlers:
            value = handler(value)

        return value
    return chained_handler

def x_test_chain_handler():
    funcs = [add_1, multi_3, add_2, multi_5, add_3, multi_2, add_4]
    sample2 = [2, 3, 5, 7, 11, 13]
    expected_output_func = lambda a: (((((((s + 1) * 3) + 2) * 5) + 3 ) * 2) + 4)

    chained_func1 = chain_handlers(funcs)

    import pdb;pdb.set_trace()

    for s in sample2:
        assert_chain_handler(chained_func1, s, expected_output_func(s))


def chain_handlers(*handlers):
    def chaining_func(acc, f):
        import pdb;pdb.set_trace()
        return f(acc)

    return functools.partial(functools.reduce, chaining_func, handlers)

def chain_handler2(*handlers):
    chaining_func = lambda acc, f: f(acc)

    return functools.partial(functools.reduce, chaining_func, handlers)


def assert_chain_handler(chain_handler, input, expected_output):
    assert chain_handler(input) == expected_output
