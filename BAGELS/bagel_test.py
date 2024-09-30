import unittest
from unittest.mock import patch
from BAGELS.bagels import get_clues, get_secretion, NUM_DIGITS


class TestBagelsGame(unittest.TestCase):

    def test_get_clues_correct_guess(self):
        self.assertEqual(get_clues('123', '123'), 'You got it!')

    def test_get_clues_pico_fermi(self):
        self.assertEqual(get_clues('321', '123'), 'Pico Fermi Pico')

    def test_get_clues_fermi(self):
        self.assertEqual(get_clues('124', '123'), 'Fermi Fermi')

    def test_get_clues_bagels(self):
        self.assertEqual(get_clues('456', '123'), 'Bagels')

    def test_get_secretion_length(self):
        self.assertEqual(len(get_secretion()), NUM_DIGITS)

    @patch('random.shuffle', lambda x: x)
    def test_get_secretion_content(self):
        self.assertEqual(get_secretion(), '123')


if __name__ == '__main__':
    unittest.main()
