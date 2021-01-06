import unittest
from . import light_changer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.subject = light_changer.LightChanger()

    def test_light_changer_set_yellow(self):
        print(self.subject.set_yellow())
        #self.assertEqual(self.subject.set_yellow(), 2)


if __name__ == '__main__':
    unittest.main()
