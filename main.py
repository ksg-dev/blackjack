import random
from clear import clear

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
            return int(score)
    else:
        return int(score)


# Final score print statement to save some repetition
def final_score(user_hand, dealer_hand, user_score, dealer_score):
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")


def main():
    playing = True
    dealer_hand = random.sample(cards, 2)
    user_hand = random.sample(cards,2)
    while playing:
        dealer_score = calculate_score(dealer_hand)
        user_score = calculate_score(user_hand)
        # check for dealer blackjack
        if dealer_score == 0:
            playing = False
            final_score(user_hand, dealer_hand, user_score, dealer_score)
            print("The Dealer got BlackJack! You Lose!")
        # Check for user blackjack
        elif user_score == 0:
            playing = False
            final_score(user_hand, dealer_hand, user_score, dealer_score)
            print("You got BlackJack! You win!")
        # Check for bust
        elif user_score > 21:
            playing = False
            final_score(user_hand, dealer_hand, user_score, dealer_score)
            print("You went over! You lose!")
        # display hand, dealer 1st card, prompt to hit or stay
        else:
            print(f"Your cards: {user_hand}, current score: {user_score}")
            print(f"Dealer's first card: {dealer_hand[0]}")
            hit = (input("Type 'y' to get another card, type 'n' to pass: "))
            # if hit, draw another card and append to hand
            if hit == 'y':
                user_hand.append(deal_card())
                user_score = calculate_score(user_hand)
            # If dealer under 17, draw card and append to hand
            if dealer_score < 17:
                dealer_hand.append(deal_card())
                dealer_score = calculate_score(dealer_hand)
            # Pass or stay
            elif hit == 'n':
                playing = False
                dealer_score = calculate_score(dealer_hand)
                user_score = calculate_score(user_hand)
                final_score(user_hand, dealer_hand, user_score, dealer_score)
                if user_score == dealer_score:
                    print("It's a draw!")
                elif dealer_score > 21:
                    print("Dealer busted! You Win!")
                elif user_score > dealer_score:
                    print("You win!")
                else:
                    print("Dealer wins, you lose!")
    # Ask player if they want to play again
    again = input("Would you like to play again? Type 'y' or 'n': ")
    if again == 'y':
        clear()
        start()
    else:
        print("Thanks for playing!")
   


def start():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        main()
    else:
        print("Thanks for playing. Goodbye.")

start()
        