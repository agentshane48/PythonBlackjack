#Jared S. Johnson  - Dictionary
#Osa     - Scoring function
#Abu     - Main function/Repeat

#This program is a text-based game of Blackjack. Enjoy.
#12/02/2014
#projectblackjack.py

# Allows exit
import sys


def main():

    # Greeting
    print('Welcome to Blackjack! Lets get started with a couple of cards!')

    # Create a deck of cards.
    deck = create_deck()

    # Get the number of cards to deal.
    num_cards = 2

    # Scoring Accumulator
    hand_score = 0


    # Deal the cards.
    deal_cards(deck, num_cards)

    # Scoring/second chance/third chance/maybe four if you have a low total
    scoring(deck, hand_score)

    # Prompts user to run program again
    again()


# The create_deck function returns a dictionary representing a deck of cards.
def create_deck():
    # Create a dictionary with each cards and its value
    # stored as a key-value pairs.

    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6, '7 of Spades':7,
            '8 of Spades':8, '9 of Spades':9, '10 of Spades':10,
            'Jack of Spades':10, 'Queen of Spades':10, 'King of Spades':10,

            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6, '7 of Hearts':7,
            '8 of Hearts':8, '9 of Hearts':9, '10 of Hearts':10,
            'Jack of Hearts':10, 'Queen of Hearts':10, 'King of Hearts':10,

            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6, '7 of Clubs':7,
            '8 of Clubs':8, '9 of Clubs':9, '10 of Clubs':10,
            'Jack of Clubs':10, 'Queen of Clubs':10, 'King of Clubs':10,

            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10,'Jack of Diamonds':10, 'Queen of Diamonds':10,
            'King of Diamonds':10,}

    # Returns the deck
    return deck


# The deal_cards function deals two initial cards for the user and accumulates
# their value and passes it back as a score.
def deal_cards(deck, number):

    # Initialize an accumulator for the hand value
    hand_score = 0

    # Deal the cards and accumulate their values.
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_score += value

    # Display the value of the hand.
    print('Value of this hand: ', hand_score)

    # Return the score for future use.
    return hand_score


# The scoring function takes the score from the first two dealt cards.
# Since the score will always be less than 21, the user will have another choice.
# It deals an additional card. If >= 21, function ends.
# If < 21, deals 4th card.
def scoring(deck, hand_score):
    
    if hand_score is 21:
        print('Blackjack! Congratulations! You have a score of 21.')
    elif hand_score > 21:
        print('Busted! Your score of', hand_score, ' is over the limit of 21. Sorry!')
    else:
        play = input('Your score is less than the limit of 21. Would you like another card?(Yes/No)')
        if play[0] is 'Y' or play[0] is 'y':
            card, value = deck.popitem()
            print(card)
            hand_score += value
            if hand_score is 21:
                print('Blackjack! Congratulations! You have a score of 21.')
            elif hand_score > 21:
                print('Busted! Your score of', hand_score, ' is over the limit of 21. Sorry!')
            else:
                play = input('Your score is less than the limit of 21. Would you like another card?(Yes/No)')
                if play[0] is 'Y' or play[0] is 'y':
                    card, value = deck.popitem()
                    print(card)
                    hand_score += value
            
        else:
            print('Thanks for playing!')


# The repeat function prompts the user and asks if they would like to play another instance of the blackjack game.
def again():
    x = input('Play again? (Yes/No)')
    if x[0] is 'Y' or x[0] is 'y':
        main()
    else:
        sys.exit(0)
        
        
        






# Call the main function.
main()


            
            
