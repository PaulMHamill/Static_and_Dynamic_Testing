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
    
    def test_suit_has_ace(self):
        self.assertEqual(1, self.card.value)

    def test_highest_card_is_returned(self):
        self.highest_card = (self.card1, self.card2)
        self.assertEqual(3, self.card2.value)

    def test_card_totals(self):
        self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 5", self.card_game.cards_total(self.cards))





