from art import logo, vs
from game_data import data
from random import choice
from replit import clear


def format_data(account):
    """Returns the data in printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}. Occupation: {account_descr}. From {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and return true or false"""
    if a_followers > b_followers:
        return guess == "A" #False if guess is "b"/alternative to "if{ guess == b; return False}"
    else:
        return guess == "B" #False if guess is "a"/alternative to "if{ guess == a; return False}"
        

score = 0
game_continue = True
account_b = choice(data) #To satisfy account_a = account_b, #random account/dictionary from the list of dictionaries

while game_continue:

    #Making account at position A become account at position be in the next round
    account_a = account_b #previous account_b becomes new account_a
    account_b = choice(data) #a new account_b value is generated
    while account_a == account_b: #incase both are generated same, a new value for account_b is generated again
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers A or B: \n").upper()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # print(is_correct)

    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're Correct. Your score: {score}")
    else:
        game_continue = False
        print(f"You're Wrong. Final score {score}")

