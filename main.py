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



# return random card from cards
def deal_card():
    return(random.choice(cards))
        

# Calculate score, check for ace sub, check for blackjack
def calculate_score(hand):
    score = sum(hand)
    if 11 in hand:
        if sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
        elif len(hand) == 2 and 10 in hand:
            return 0
        else:
            return 11
    else:
        return score

def main():
    playing = True
    dealer_hand = random.sample(cards, 2)
    user_hand = random.sample(cards,2)
    while playing:
        dealer_score = int(calculate_score(dealer_hand))
        user_score = int(calculate_score(user_hand))
        # check for dealer blackjack
        if dealer_score == 0:
            playing = False
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
            print("The Dealer got BlackJack! You Lose!")
        # Check scores
        elif user_score == 0:
            playing = False
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
            print("You got BlackJack! You win!")
        elif user_score > 21:
            playing = False
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
            print("You went over! You lose!")
        else:
            hit = ("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                user_hand.append(deal_card())
                # Test print
                print(f"user_hand: {user_hand}, score: {user_score}")
                 # Test print
                print(f"dealer_hand: {dealer_hand}, score: {dealer_score}")
            if dealer_score < 17:
                dealer_hand.append(deal_card())
            
   



start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start == 'y':
    main()
else:
    print("Thanks for playing. Goodbye.")
        