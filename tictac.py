#TIC TAC TOE WHERE COMPUTER NEVER LOSES
#Hasnain Shahid FA21-BAI-018
#Tahawar Khattak FA21-BAI-019
#Submitted to Sir Khurram Iqbal



# Importing random for Toss
import random

#Formation of the Game Board 
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


#Condition for wins
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

#Player Moves
def playerMove():
    global symbol
    run = True
    while run:
        move = input(f'Please select a position to place an {symbol.upper()} (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter(f'{symbol}', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            
# Computer moves and Minimax Algorithim
def compMove():
    global comp_symbol
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
#Checking for tie
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    global symbol
    global comp_symbol
    print('Welcome to Tic Tac Toe!')
    printBoard(board)
    
    
#Statements for the winners and ties
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print(f'Sorry, {comp_symbol} won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                if symbol=="x":
                    insertLetter('O', move)
                    print(f'Computer placed an {comp_symbol} in position', move , ':')
                    printBoard(board)
                else:
                    insertLetter('X', move)
                    print(f'Computer placed an {comp_symbol} in position', move , ':')
                    printBoard(board)
        else:
            print(f'{symbol.upper()} won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')
#Taking inputs from user asking his/her name, symbol , and heads or tails for toss
while True:
    global symbol
    global comp_symbol
    answer = input('Do you want to play again? (Y/N)')
    name_of_player= input('Enter your name: ')
    symbol=input('Choose a symbol X or O; ')
    if symbol.lower()=='x' :
        comp_symbol='o'
    if symbol.lower()=='o':
        comp_symbol='x'
    from random import random
    guess = input('Pick heads or tails and then press enter to play: ')
    winner="-"
    if random() > 1:
        winner == "Tails"
        print("Tails wins!")
    else:
        winner == "Heads"
        print('Heads wins!')

    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
