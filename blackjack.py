# import
import random
from clear_screen import clear
from art import logo
import time
import progressbar

# progress bar
def progress():
    print("DEALING CARDS...")
    for i in progressbar.progressbar(range(2), redirect_stdout=True):
        time.sleep(0.5)

# deal card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# calculate score. remember blackjack rules!!
def calculate(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# compare scenarios
def compare(user_score,computer_score):
    if user_score == computer_score:
        return "User and computer have same score so draw 🙃🙂"
    elif computer_score == 0:
        return "Computer got blackjack! User loses 😖💢"
    elif user_score == 0:
        return "User got a blackjack! User wins 🤠💃"
    elif user_score > 21:
        return "User went over so user loses 😠😭"
    elif computer_score > 21:
        return "Computer went over so user wins 🎉🥳 "
    elif user_score > computer_score:
        return "User wins 💛😎"
    else:
        return "User loses 😱😢"


# game
def game():
    game_over = False
    users_cards = []
    computers_cards = []
    print(logo)
    progress()

    for number in range(2):
        users_cards.append(deal_card())
        computers_cards.append(deal_card())

    while game_over == False:
        user_score = calculate(users_cards)
        computer_score = calculate(computers_cards)
        outcome = compare(user_score,computer_score)
        print()
        print(f"User's current cards are: {users_cards} and score is: {user_score}.")
        print(f"Computer's first card is: {computers_cards[0]}.")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            game_over = True
        else:
            print()
            ask = input("Would you like to deal another card? Yes or no? ").lower()
            if ask == "yes":
                print()
                progress()
                users_cards.append(deal_card())
            elif ask == "no":
                game_over = True
            else:
                print("invalid choice")

    user_score = calculate(users_cards)
    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate(computers_cards)

    # final outcome
    print()
    print("----Game Over----")
    print(f"Your final hand is {users_cards} and score is {user_score}.")
    print(f"Computer's final hand is {computers_cards} and score is {computer_score}.")
    print(outcome)


game()
print()
while input("Do you want to play another game? Yes or no? ").lower() == "yes":
    clear()
    game()
else:
    print()
    print("Thanks for playing! 😁")
    print()

