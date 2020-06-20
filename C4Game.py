import sys
from termcolor import colored

class C4Game:

    # List of shapes (characters) and colors that players will be assigned
    colorMap = [
        colored('O', 'blue'),
        colored('O', 'red'),
    ]

    def __init__(self, players=1, boardWidth=7, boardHeight=8, winLength=4, turn=0, *names):
        self.players = players  # Number of players
        if players > len(self.colorMap):
            raise Exception("Too many players, not enough colors")
        if len(names) != players:
            raise Exception(f"{len(names)} player names provided, but {players} players")
        self.playerArray = [Player(i, names[i]) for i in range(players)]
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.winLength = winLength
        if winLength > max(boardWidth, boardHeight):
            print(f"winLength {winLength} is too large for {boardWidth}x{boardHeight} board.  No one will be able to win.", sys.stderr)
        self.board = self.createBoard()
        self.turn = turn # Whose turn it is, as an integer; takes values 0,...,players - 1

    
    def __repr__(self):
        return f"C4Game(players = {self.players}, baordWidth = {self.boardWidth}, boardHeight = {self.boardHeight}, winLength = {self.winLength}, turn = {self.turn}, names = {self.names}"
    
    def __str__(self):
        return repr(self)

    def createBoard(self):
        # List of lists of blank spots ('-') that will be filled in with players' pieces
        return [['-' for i in range(self.boardWidth)] for j in range(self.boardHeight)]

    def printBoard(self):
        # Prints the board in its current state
        for row in range(self.boardHeight):
            for col in range(self.boardWidth):
                print(self.board[self.boardHeight - 1 - row][col], end=" ")
            print("")

    def play(self, column: int):
        """column is the column that was chosen for dropping a piece into.  Can take values 1,...,boardWidth.  Board will be modified and the turn will be changed."""
        if (column > self.boardWidth or column == 0):
            print(f"Column must be between 1 and {self.boardWidth}", sys.stderr)
            return
        if self.board[self.boardHeight-1][column-1] != '-':
            print("That column is full, pick a different column", sys.stderr)
            return
        for height in range(self.boardHeight):
            if self.board[height][column-1] == '-':
                self.board[height][column-1] = self.colorMap[self.turn]
                break
        self.turn = (self.turn + 1) % self.players

    def allPossibleWins(self):
        """A set of all possible ways of winning, given the board dimensions.  Each way of winning is itself represented as a frozenset (of size winLength) of tuples, where each tuple is the coordinates of one of the board spots included in the winning line.

        For example, if we have a board of size 3x3, and winLength = 2, then the possible ways of winning are:

        _______________________

        horizontal lines:
        
        * * *
        * * *
        O O *  

        * * *
        * * *
        * O O

        * * *
        O O *
        * * *

        * * *
        * O O
        * * *

        O O *
        * * *
        * * *

        * O O
        * * *
        * * *

        which will be represented by the frozensets

        {(0,0), (1,0)}
        {(1,0), (2,0)}
        {(0,1), (1,1)}
        {(1,1), (2,1)}
        {(0,2), (1,2)}
        {(1,2), (2,2)}

        _______________________

        vertical lines:

        * * *
        O * *
        O * *

        O * *
        O * *
        * * *

        * * *
        * O *
        * O *

        * O *
        * O *
        * * *

        * * *
        * * O
        * * O

        * * O
        * * O
        * * *

        which will be represented by the frozensets

        {(0,0), (0,1)}
        {(0,1), (0,2)}
        {(1,0), (1,1)}
        {(1,1), (1,2)}
        {(2,0), (2,1)}
        {(2,1), (2,2)}

        _______________________

        diagonal up lines:

        * * *
        * O *
        O * *

        * * *
        * * O
        * O *

        * O *
        O * *
        * * *

        * * O
        * O *
        * * *

        which will be represented by the frozensets

        {(0,0), (1,1)}
        {(1,0), (2,1)}
        {(0,1), (1,2)}
        {(1,1), (2,2)}

        _______________________

        diagonal down lines:

        * * *
        O * *
        * O *

        * * *
        * O *
        * * O

        O * *
        * O *
        * * *

        * O *
        * * O
        * * *

        which will be represented by the frozensets

        {(0,1), (1,0)}
        {(1,1), (2,0)}
        {(0,2), (1,1)}
        {(1,2), (2,1)}

        _______________________

        """
        horizontalWins = {}
        # for each horizontalWinTuple: (must figure these out based on board size)
            # horizontalWins.add(horizontalWinTuple)
        verticalWins = {}
        # for each verticalWinTuple: (must figure these out based on board size)
            # verticalWins.add(verticalWinTuple)
        diagonalUpWins = {}
        # for each diagonalUpWinTuple: (must figure these out based on board size)
            # diagonalUpWins.add(diagonalUpWinTuple)
        diagonalDownWins = {}
        # for each diagonalDownWinTuple: (must figure these out based on board size)
            # diagonalDownWins.add(diagonalDownWinTuple)
        allWins = {}
        allWins = allWins.union(horizontalWins, verticalWins, diagonalUpWins, diagonalDownWins)
        return allWins


class Player:

    def __init__(self, color_name: int, name=""):
        self.name = name
        self.color = C4Game.colorMap[color_name]

if __name__ == '__main__':
    game = C4Game(players = 2)
    # game.printBoard()
    game.play(3)
    # game.printBoard()
    game.play(3)
    # game.printBoard()
    game.play(2)
    # game.printBoard()
    game.play(2)
    game.play(3)
    game.printBoard()
