from mockito import mock, verify
import unittest

from helloworld import helloworld

class HelloWorldTest(unittest.TestCase):
    """docstring for HelloWorldTest"""
    def test_should_issue_hello_world_message(self):
        """docstring for test_should_issue_hello_world_message"""
        out = mock()
        helloworld(out)
        verify(out).write("Hello world of Python\n")
