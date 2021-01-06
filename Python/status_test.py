import unittest
from mock import patch
from . import status
from . import light_changer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.subject = status.Status()

    def test_status_inits_to_free(self):
        self.assertEqual(self.subject.current(), "Free")
        self.assertIsInstance(self.subject.changer, light_changer.LightChanger)

    def test_status_changes_to_Interruptable(self):
        with patch.object(self.subject.changer, 'set_yellow') as mock:
            self.subject.set_interruptable()
            mock.assert_called_once()

        self.assertEqual(self.subject.current(), "Interrupt-able")

    def test_status_changes_to_Busy(self):
        with patch.object(self.subject.changer, 'set_red') as mock:
            self.subject.set_busy()
            mock.assert_called_once()

        self.assertEqual(self.subject.current(), "Busy")

    def test_status_changes_back_to_Free(self):
        self.subject.set_busy()
        self.assertEqual(self.subject.current(), "Busy")
        with patch.object(self.subject.changer, 'set_green') as mock:
            self.subject.set_free()
            mock.assert_called_once()

        self.assertEqual(self.subject.current(), "Free")

    def test_status_reports_if_free(self):
        self.assertTrue(self.subject.is_free())
        self.assertFalse(self.subject.is_busy())
        self.assertFalse(self.subject.is_interruptable())

    def test_status_reports_if_interruptable(self):
        self.subject.set_interruptable()
        self.assertTrue(self.subject.is_interruptable())
        self.assertFalse(self.subject.is_busy())
        self.assertFalse(self.subject.is_free())

    def test_status_reports_if_busy(self):
        self.subject.set_busy()
        self.assertTrue(self.subject.is_busy())
        self.assertFalse(self.subject.is_interruptable())
        self.assertFalse(self.subject.is_free())


if __name__ == '__main__':
    unittest.main()
