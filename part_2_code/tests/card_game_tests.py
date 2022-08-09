import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card = Card("hearts", 1)
        self.card1 = Card("hearts", 2)
        self.card2 = Card("hearts", 3)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame()
    
    def test_check_for_ace(self):
        self.assertEqual(1, self.card_game.check_for_ace(self.card))

    def test_highest_card(self):
        self.highest_card = (self.card1, self.card2)
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_card_totals(self):
        self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 5", self.card_game.cards_total(self.cards))





