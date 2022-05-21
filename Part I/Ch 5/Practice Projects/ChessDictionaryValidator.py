"""
Chess Dictionary Validator 
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. 
Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid. 
A valid board will have exactly one black king and exactly one white king. 
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece cant be on space '9z'. 
The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
This function should detect when a bug has resulted in an improper chess board.

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 127). No Starch Press. Kindle Edition. 
"""

theBoard = {
    '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '3a': ' ', '3b': ' ', '3c': ' ', '3d': ' ', '3e': ' ', '3f': ' ', '3g': ' ', '3h': ' ',
    '4a': ' ', '4b': ' ', '4c': ' ', '4d': ' ', '4e': ' ', '4f': ' ', '4g': ' ', '4h': ' ',
    '5a': ' ', '5b': ' ', '5c': ' ', '5d': ' ', '5e': ' ', '5f': ' ', '5g': ' ', '5h': ' ',
    '6a': ' ', '6b': ' ', '6c': ' ', '6d': ' ', '6e': ' ', '6f': ' ', '6g': ' ', '6h': ' ',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking', '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook',
    }

def isValidChessBoard(board):
    print(
        board['1a'] + '|' + board['1b'] + '|' + board['1c'] + '|' + board['1d'] + '|' + board['1e'] + '|' + board['1f'] + '|' + board['1g'] + '|' + board['1h'])
    print('-+-+-+-+-+-+-+-')
    print(
        board['2a'] + '|' + board['2b'] + '|' + board['2c'] + '|' + board['2d'] + '|' + board['2e'] + '|' + board['2f'] + '|' + board['2g'] + '|' + board['2h'])
    print('-+-+-+-+-+-+-+-')
    print(
        board['3a'] + '|' + board['3b'] + '|' + board['3c'] + '|' + board['3d'] + '|' + board['3e'] + '|' + board['3f'] + '|' + board['3g'] + '|' + board['3h'])
    print('-+-+-+-+-+-+-+-')
    print(
        board['4a'] + '|' + board['4b'] + '|' + board['4c'] + '|' + board['4d'] + '|' + board['4e'] + '|' + board['4f'] + '|' + board['4g'] + '|' + board['4h'])
    print('-+-+-+-+-+-+-+-')
    print(
        board['5a'] + '|' + board['5b'] + '|' + board['5c'] + '|' + board['5d'] + '|' + board['5e'] + '|' + board['5f'] + '|' + board['5g'] + '|' + board['5h'])
    print('-+-+-+-+-+-+-+-')
    print(
        board['6a'] + '|' + board['6b'] + '|' + board['6c'] + '|' + board['6d'] + '|' + board['6e'] + '|' + board['6f'] + '|' + board['6g'] + '|' + board['6h'])
    print('-+-+-+-+-+-+-+-')
    print(
        board['7a'] + '|' + board['7b'] + '|' + board['7c'] + '|' + board['7d'] + '|' + board['7e'] + '|' + board['7f'] + '|' + board['7g'] + '|' + board['7h'])
    print('-+-+-+-+-+-+-+-')
    print(
        board['8a'] + '|' + board['8b'] + '|' + board['8c'] + '|' + board['8d'] + '|' + board['8e'] + '|' + board['8f'] + '|' + board['8g'] + '|' + board['8h'])
    print('-+-+-+-+-+-+-+-')

    while True:
        print('Enter move: (blank to quit)')
        space = input()
        if space == '':
            break
        
        if space in theBoard:
            if theBoard[space] == ' ':
                print("nothing is here")
                continue            
            print(theBoard[space].title() + ' is on that spot!')

        else:
            print(f"{space} is not in the board")
            

isValidChessBoard(theBoard)
