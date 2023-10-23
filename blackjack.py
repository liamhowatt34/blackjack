import random
import time

def generate_deck() -> list:
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    deck = [i for i in ranks for _ in range(4)]
    random.shuffle(deck)
    return deck


def deal_game(deck) -> list:
    player_card1 = deck.pop(0)
    dealer_card1 = deck.pop(0)
    player_card2 = deck.pop(0)
    dealer_card2 = deck.pop(0)
    return [dealer_card1,dealer_card2],[player_card1,player_card2]


def count_score(hand) -> int:
    score = 0
    aces = 0
    for card in hand:
        if card == 'A':
            score += 11
            aces += 1
        elif card.isalpha():
            score += 10
        else:
            score += int(card)
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score
        

def user_command() -> str:
    valid_inputs = ('h','s','q')
    while True:
        user_input = input('Hit or Stand?(h/s): ').lower()
        if user_input in valid_inputs:
            return user_input
        

def hit(player_score,player_hand,shuffled_deck) -> int:
    player_hand.append(shuffled_deck.pop(0))
    player_score = count_score(player_hand)
    return player_score


def declare_winner(player_score,dealer_score) -> None:
    if player_score > dealer_score: print('Player wins!!')
    elif player_score == dealer_score: print('Push.')
    else: print('Dealer Wins..')


def play_continue() -> str:
    valid_inputs = ('y','n')
    while True:
        user_input = input('Play Again?(y/n): ').lower()
        if user_input in valid_inputs:
            return user_input


def game() -> None: 
    wins_player = 0
    wins_dealer = 0
    
    while True:
        shuffled_deck = generate_deck()

        dealer_hand,player_hand = deal_game(shuffled_deck)

        print(f"\nDealer:  {dealer_hand[0]}\n")
        print(f"Player:  {' '.join(player_hand)}\n")

        player_score = count_score(player_hand)
        dealer_score = count_score(dealer_hand)
        
        playing = True
        while playing:
            if player_score == 21:
                print('Player Wins!!')
                wins_player += 1
                playing = False
                break

            if dealer_score == 21:
                print(f"Dealer: {' '.join(dealer_hand)}")
                print('Dealer Wins!!')
                wins_dealer += 1
                playing = False
                break
            
            player_input = user_command()
            print('\n')

            if player_input == 'q':
                playing = False

            if player_input == 'h':
                player_score = hit(player_score,player_hand,shuffled_deck)
                print(f"Player:{' '.join(player_hand)}")
                if player_score > 21:
                    print(f"\nDealer: {' '.join(dealer_hand)}")
                    print('Dealer Wins..')
                    wins_dealer += 1
                    playing = False

            if player_input == 's':
                if dealer_score >= 17 and dealer_score <= 21:
                    print(f"Dealer: {' '.join(dealer_hand)}")
                    declare_winner(player_score,dealer_score)
                    if player_score > dealer_score:
                        wins_player += 1
                    if player_score < dealer_score:
                        wins_dealer += 1
                    playing = False
                else:    
                    while dealer_score < 17:
                        dealer_score = hit(dealer_score,dealer_hand,shuffled_deck)
                        if dealer_score >= 17 and dealer_score <= 21:
                            print(f"Dealer: {' '.join(dealer_hand)}")
                            declare_winner(player_score,dealer_score)
                            if player_score > dealer_score:
                                wins_player += 1
                            if player_score < dealer_score:
                                wins_dealer += 1
                            playing = False
                        if dealer_score > 21:
                            print(f"Dealer: {' '.join(dealer_hand)}")
                            print('Player Wins!!')
                            wins_player += 1
                            playing = False

        time.sleep(1)
        print(f'\nPlayer Wins:  {wins_player}')
        print(f'Dealer Wins:  {wins_dealer}')
        print('-------------------')
        print('Thanks for playing.\n')

        play_again = play_continue()

        if play_again == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    game()