'''
07.01 Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
    subclass the data structures to implement blackjack.
'''

import random

# Card class represents an individual card with a suit and a rank.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Deck class represents a collection of cards and provides methods to shuffle and deal cards.
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        # Create a standard deck of cards
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if not self.is_empty():
            return self.cards.pop()
        return None

    def is_empty(self):
        return len(self.cards) == 0


# BlackjackCard subclass of Card that assigns values to the ranks, considering the rules of Blackjack.
class BlackjackCard(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)
        self.value = self.get_value()

    def get_value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)


# BlackjackDeck subclass of Deck that uses BlackjackCard instead of Card to create the deck.
class BlackjackDeck(Deck):
    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        # Create a standard deck of Blackjack cards
        self.cards = [BlackjackCard(suit, rank) for suit in suits for rank in ranks]


# Player class represents a player in the Blackjack game.
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        return sum(card.value for card in self.hand)

    def clear_hand(self):
        self.hand = []


# Implementing the game logic:

def play_blackjack():
    player_name = input("Enter player name: ")
    player = Player(player_name)
    deck = BlackjackDeck()
    deck.shuffle()
    
    print("Press 'q' anytime to finish the game!")

    while True:
        player.clear_hand()

        # Deal two cards to the player
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())

        print(f"{player.name}'s hand:")
        for card in player.hand:
            print(f'    {card}')

        # Check if the player's initial hand is a blackjack
        if player.get_hand_value() == 21:
            print("\n  Blackjack! You win!\n")
        else:
            # Ask the player if they want to hit or stand
            while True:
                choice = input("\n  Do you want to hit or stand? (h/s): ").lower()
                if choice == 'h':
                    # Deal one more card
                    player.add_card(deck.deal_card())
                    print(f"\n\n{player.name}'s hand:")
                    for card in player.hand:
                        print(f'    {card}')

                    # Check if the player busted (hand value > 21)
                    if player.get_hand_value() > 21:
                        print("  Busted! You lose!\n")
                        break
                elif choice == 's':
                    # Player chose to stand, end the game
                    dealer_hand = []
                    dealer_hand.append(deck.deal_card())
                    dealer_hand.append(deck.deal_card())
                    print("\nDealer's hand:")
                    print(f'    {dealer_hand[0]}')  # Show only one of the dealer's cards

                    # Dealer hits until the hand value is at least 17
                    while sum(card.value for card in dealer_hand) < 17:
                        dealer_hand.append(deck.deal_card())

                    print("Dealer's hand:")
                    for card in dealer_hand:
                        print(f'    {card}')

                    # Determine the winner
                    player_value = player.get_hand_value()
                    dealer_value = sum(card.value for card in dealer_hand)
                    if dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
                        print("\n  Congratulations! You win!\n")
                    else:
                        print("\n  Sorry, you lose!\n")
                    break
                elif choice == 'q':
                    print("\nThanks for playing! See you next time.")
                    return
                else:
                    print("Invalid input. Please enter 'h' for hit or 's' for stand or 'q' to quit.")

if __name__ == "__main__":
    play_blackjack()