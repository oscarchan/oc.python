from mock import Mock, MagicMock, patch
import types

print """
"""

def test_mock_method_reply():
    class TestClass:
        def method(self):
            print "test_mock_method.TestClass.method"
        def something(self):
            pass

    test_object = TestClass()
    test_object.method = MagicMock(name='method')
    returned = test_object.method(2, 3, 4, key='value')

    test_object.method.assert_called_once_with(2, 3, 4, key='value')

def test_mock_method_stub():
    class TestClass:
        def method(self):
            print "test_mock_stub.TestClass.method"
            print 456

    def method_mock():
        print "test_mock_stub.method_mock"
        return 123

    test_object = TestClass()
    test_object.method = Mock(side_effect=method_mock)
    
    returned = test_object.method()

    test_object.method.assert_called_once_with()
    assert returned == 123

def test_override_method():
    class TestClass:
        def method(self):
            print "test_mock_stub.TestClass.method"
            print 456

    def method_mock(self):
        print "test_mock_stub.method_mock"
        return 123

    test_object = TestClass()
    test_object.method = types.MethodType(method_mock, test_object)
    
    returned = test_object.method()

    assert returned == 123
