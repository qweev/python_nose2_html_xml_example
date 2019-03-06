import unittest
import time

class testowySuitepack(unittest.TestCase):
    def test_pierwszypack(self):
        time.sleep(1)
        assert True
    test_pierwszypack.flags = ['red', 'green']

    def test_dwapack(self):
        time.sleep(2)
        assert True
    test_dwapack.flags = ['ssreds', 'green']



