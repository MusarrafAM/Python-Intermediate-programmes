# Tic Tac Toe

winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def check_winner(user_list):
    for each_winning_list in winning_combinations:
        if each_winning_list[0] in user_list and each_winning_list[1] in user_list and each_winning_list[2] in user_list:
            return True
    return False  # Moved outside the for loop, after checking all winning combinations



def play_game():
    game = {
        0: "⬜", 1: "⬜", 2: "⬜", 3: "⬜", 4: "⬜", 5: "⬜", 6: "⬜", 7: "⬜", 8: "⬜"
    }

    print("Welcome to Musarraf's tic tac toe")
    print(
        f"{game[0]} | {game[1]} | {game[2]}\n-----------\n{game[3]} | {game[4]} | {game[5]}\n-----------\n{game[6]} | {game[7]} | {game[8]}")

    gameIsOn = True
    player1_combination = []
    player2_combination = []

    while gameIsOn:
        alreadyNotTaken = True
        while alreadyNotTaken:
            player1 = int(input("Enter User 1 position (0 to 8)"))
            if player1 > 8 or  player1 < -1:
                print("Enter correct number")
            else:
                if game[player1] == "⬜":
                    player1_combination.append(player1)
                    game[player1] = "X"
                    print(
                        f"{game[0]} | {game[1]} | {game[2]}\n-----------\n{game[3]} | {game[4]} | {game[5]}\n-----------\n{game[6]} | {game[7]} | {game[8]}")
                    alreadyNotTaken = False
                    if check_winner(player1_combination):
                        print("Player 1 is the winner")
                        return
                else:
                    print("Already selected that box")
                    alreadyNotTaken = True

        alreadyNotTaken = True
        while alreadyNotTaken:
            player2 = int(input("Enter User 2 position (0 to 8)"))
            if player2 > 8 or  player2 < -1:
                print("Enter correct number")
            else:
                if game[player2] == "⬜":
                    player2_combination.append(player2)
                    game[player2] = "O"
                    print(
                        f"{game[0]} | {game[1]} | {game[2]}\n-----------\n{game[3]} | {game[4]} | {game[5]}\n-----------\n{game[6]} | {game[7]} | {game[8]}")
                    alreadyNotTaken = False
                    if check_winner(player2_combination):
                        print("Player 2 is the winner")
                        return
                else:
                    print("Already selected that box")
                    alreadyNotTaken = True


play_game()
