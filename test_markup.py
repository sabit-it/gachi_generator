import unittest
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import markup as nav


class TestMarkup(unittest.TestCase):
    def test_main_menu(self):
        keyboard = nav.mainMenu
        self.assertIsInstance(keyboard, ReplyKeyboardMarkup)
        self.assertEqual(len(keyboard.keyboard), 1)
        self.assertEqual(keyboard.keyboard[0][0].text, "Generate Gachi")


if __name__ == "__main__":
    unittest.main()
