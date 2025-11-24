import random

board = {
    4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 51: 67, 63: 81, 71: 91,   # ladders
    17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 79   # snakes
}

p1 = 0
p2 = 0
turn = 1

def roll():
    return random.randint(1, 6)

print("Snake and Ladder Game")
print("Player 1 vs Player 2\n")

while True:
    if turn == 1:
        input("Player 1 press enter to roll...")
        d = roll()
        print("Player 1 got:", d)
        p1 = p1 + d
        if p1 in board:
            p1 = board[p1]
        if p1 > 100:
            p1 = p1 - d
        print("Player 1 position:", p1)
        if p1 == 100:
            print("Player 1 Wins!")
            break
        turn = 2

    else:
        input("Player 2 press enter to roll...")
        d = roll()
        print("Player 2 got:", d)
        p2 = p2 + d
        if p2 in board:
            p2 = board[p2]
        if p2 > 100:
            p2 = p2 - d
        print("Player 2 position:", p2)
        if p2 == 100:
            print("Player 2 Wins!")
            break
        turn = 1
