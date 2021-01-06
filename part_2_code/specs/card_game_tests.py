import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 3)
        self.card2 = Card("Clubs", 1)

        self.cards = [self.card1, self.card2]

        self.card_game = CardGame()

    def test_check_for_ace_function(self):
        self.assertTrue(self.card_game.check_for_ace(self.card2))



    def test_highest_card_function(self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))