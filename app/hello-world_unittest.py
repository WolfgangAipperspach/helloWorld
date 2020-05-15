
import unittest
import helloWorld

class TestStringMethods(unittest.TestCase):
    def test_helloworld(self):
        hw = helloWorld.HelloWorld()
        self.assertEqual("HelloWorld",hw.run())

    def __disabled_test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def __disabled_test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def __disabled_test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()



