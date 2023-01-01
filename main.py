import random
 
def deal_card() :
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    cards_random = random.choice(cards)

    return cards_random


def calculate(cards):


    if sum(cards) == 21 and len(cards)== 2 :
       return 0 
   

    if 11 in cards and sum(cards) > 21 :
            cards.remove(11)
            cards.append(1)
    return sum(cards) 

# Deal the user and computer 2 cards each using deal_card() and append().


user_card = []
computer_card = []

is_game_over = False

for i in range (2) :
    user_card.append( deal_card())

    computer_card.append( deal_card()) 

def compare(user_score, computer_score) :
    if user_score == computer_score :
        return "DRAW"
    elif computer_score == 0 :
        return "Lose , opponent has blackjack👌"
    elif user_score == 0 :
         return "Lose , opponent has blackjack👌"
    elif user_score > 21 :
        return "You went over😭😭😭😭😭"
    elif computer_score > 21 :
          return "You went over😭😭😭😭😭"
    elif user_score > computer_score :
        return "User win👌"
    else :
          return "You lose😭"


while not is_game_over :
# Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

        user_score = calculate(user_card)

        computer_score = calculate(computer_card)

        print(f"Your card :{user_card} Current score : {user_score}")
        print(f"Computer's  card :{computer_card} Current score : {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
         is_game_over = True 

        else :
        #     #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
         while computer_score != 0 and computer_score < 17 :
            computer_card.append(deal_card())
            computer_score = calculate(computer_card)

        print(f"Your card :{user_card} Current score : {user_score}")
        print(f"Computer's  card :{computer_card} Current score : {computer_score}")
        print(compare(user_score, computer_score) )

        user_type =   input("Type 'y' to get another card typt 'n' to pass\n")


        if user_type == 'y' :
              user_card.append(deal_card())
        else :
               is_game_over = True





