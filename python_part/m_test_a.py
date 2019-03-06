import unittest
import time

class testowySuite(unittest.TestCase):
    def test_pierwszy(self):
        """
        opis ipis
        opis
        pips
        :return:
        """
        print ("sdsdsdsd")
        time.sleep(1)
        assert True
    test_pierwszy.flags = ['red', 'green']

    def test_dwa(self):
        """
        jakis tak opis
        cos tam
        :return: wynik
        """
        time.sleep(2)
        assert False
    test_dwa.flags = ['red', 'green']



