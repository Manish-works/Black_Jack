import random 
from BJ import cards_img
from BJ import cards_face_img

digi_art = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                       _/ |                
                      |__/                 
"""

#Cards
cards = [9, 8, 7, 6, 5, 4, 3, 2, 0, 0, 0, 0, 0]
face_cards = {"King" : 10, "Queen" : 10, "Jack" : 10, "Ace" : 10, 10 : 10}


#Decks
comp_cards = []
your_cards = []
comp_cards_visual = []
your_cards_visual = []

def card_visual(peti):
    card_images = []  # List to store the card images as strings
    for patta in peti:
        if patta in face_cards: 
            key_list = list(face_cards.keys())  
            card_index = key_list.index(patta)  
            this_card = cards_face_img[card_index]  
            card_images.append(this_card)
        elif patta in cards:  
            card_index = cards.index(patta)  
            this_card = cards_img[card_index]  
            card_images.append(this_card)
    
    # Join all card images into a single string for display
    return "\n".join(card_images)



#Draw: Function to draw cards.
def draw():
    card = random.choice(cards)
    if card == 0:
        face_card = random.choice(list(face_cards.keys()))
        return face_card
    else:
        return card


#Total Value: Fuction to calculate and comapre total deck value.
def total_value(deck):
    value = 0
    for patta in deck:
        if patta in face_cards:
            if patta == "Ace":
                if value + 11 < 22:
                    value += 11
                else:
                    value += 1
            else:
                value += face_cards[patta]
        else:
            value += patta
    return value 


#Start of Game. Two Cards are drawn here for both comp and player.
print(digi_art)
start = input("Press \"Y\" to play a game of Black Jack!: ").lower()

if start == "y":
    # Player draws two cards
    your_cards.append(draw())
    your_cards.append(draw())
    your_card_total = total_value(your_cards)

    # Display player's cards visually
    your_cards_visual_str = card_visual(your_cards)
    print(f"Your cards are:\n{your_cards_visual_str} and your total is {your_card_total}")

    # Dealer draws two cards
    comp_cards.append(draw())
    comp_cards.append(draw())

    # Display dealer's first card visually
    if comp_cards:  # Check if there is at least one card in comp_cards
        print(f"Dealer's 1st card is:\n{card_visual([comp_cards[0]])}")
    else:
        print("Dealer has no cards.")



#Continuing with game: Player has choice to hit or stand.
cont = True

while cont == True:
    choice = input("Press \"Y\" to HIT and \"N\" to STAND: ").lower()
    
    if choice == "y":
        print("\n" * 20)
    #Player cards are added to the cards list.
        your_cards.append(draw())
        your_card_total = total_value(your_cards)
        # Display player's cards visually
        your_cards_visual_str = card_visual(your_cards)
        print(f"Your cards are:\n{your_cards_visual_str} and your total is {your_card_total}")
        
        #Check if player is busted?
        if your_card_total > 21:
            print("You have been busted! GAME OVER!")
            cont = False
            break
        else:
            comp_card_total = total_value(comp_cards)
            if comp_card_total < 17:
            #Comp cards are added to the cards list.
                comp_cards.append(draw())
                comp_card_total = total_value(comp_cards)
                print("Dealer Drew!")
                
                #Check if Comp is busted?
                if comp_card_total > 21:
                    print("Dealer has been been busted! GAME OVER!")
                    print(f"Dealer's card are:\n{card_visual(comp_cards)}")
                    print(f"Dealer's cards are {comp_cards} and Dealer's total is {comp_card_total}")
                    break
            else:
                print("Dealer chooses to STAND!")
    elif choice == "n":
        print("\n" * 20)
        cont2 = True 
        while cont2 == True:
            comp_card_total = total_value(comp_cards)
            if comp_card_total < 17:
                #Comp cards are added to the cards list.
                    comp_cards.append(draw())
                    comp_card_total = total_value(comp_cards)
                    
                    #Check if Comp is busted?
                    if comp_card_total > 21:
                        print(f"Dealer's card are:\n{card_visual(comp_cards)}")
                        print(f"Dealer's cards are {comp_cards} and Dealer's total is {comp_card_total}")
                        print("Dealer has been busted! GAME OVER!")
                        cont2 = False 
                        cont = False
                        break
            else:
                print(f"Dealer's card are:\n{card_visual(comp_cards)}")
                print(f"Dealer's cards are {comp_cards} and Dealer's total is {comp_card_total}")
                print("Dealer chooses to STAND!")
                cont2 = False
                cont = False 

#Decesion Time
if your_card_total > 21:
    print("You LOST!")
elif comp_card_total > 21:
    print("You WON!")
elif 22 > comp_card_total > your_card_total:
    print("You LOST!")
elif 22 > your_card_total > comp_card_total:
    print("You WON!")
else:
    print("TIE")