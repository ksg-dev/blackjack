import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []

user_hand = []
playing = True


# return random card from cards
def deal_card(count):
    for i in range(count):
        dealer_hand.append(random.choice(cards))
        user_hand.append(random.choice(cards))
    return dealer_hand, user_hand
        



# Determine winner once scores are final
def winner():
    pass

def main():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'n':
        return
    elif start == 'y':
        dealer_hand, user_hand = deal_card(2)
        dealer_score = sum(dealer_hand)
        user_score = sum(user_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {dealer_hand[0]}")
        hit = ("Type 'y' to get another card, type 'n' to pass: ")
        # Test print
        print(f"dealer score: {dealer_score}")
        if hit == 'y':
            user_hand.append(deal_card(1))
    # Test print
    print(f"dealer hand: {dealer_hand}")
    # Test print
    print(f"user hand: {user_hand}")



main()
        