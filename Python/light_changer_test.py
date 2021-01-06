import unittest
from . import light_changer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.subject = light_changer.LightChanger()

    def test_light_changer_set_green(self):
        self.assertEqual(self.subject.set_green(), 0)

    def test_light_changer_set_red(self):
        self.assertEqual(self.subject.set_red(), 0)

    def test_light_changer_set_yellow(self):
        self.assertEqual(self.subject.set_yellow(), 0)


if __name__ == '__main__':
    unittest.main()
