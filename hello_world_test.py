import unittest
import hello_world


class MyTestCase(unittest.TestCase):
    def test_global_func(self):
        self.assertEqual(hello_world.greeting(), "hello world")

    def test_class_func(self):
        self.assertEqual(hello_world.HelloWorld().greeting(), "hello world")


if __name__ == '__main__':
    unittest.main()
