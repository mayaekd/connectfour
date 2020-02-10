import sys
from termcolor import colored

class C4Game:
    colorMap = [
        colored('O', 'blue'),  # Gray
        colored('O', 'red'),  # Red
    ]

    def __init__(self, players=1, boardWidth=7, boardHeight=8, winLength=4, turn=0):
        self.players = players
        if players > len(self.colorMap):
            raise Exception("Too many players, not enough colors")
        self.playerArray = [Player(i) for i in range(players)]
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.winLength = winLength
        self.board = self.createBoard()
        self.turn = turn

    #
    # def __repr__(self):
    #     return f"C4Node({self.player}, {self.state}, {repr(nodearray)})"
    #
    # def __str__(self):
    #     return f"Player: {self.player}, State: {self.state}"

    def createBoard(self):
        return [['-' for i in range(self.boardWidth)] for j in range(self.boardHeight)]

    def printBoard(self):
        for row in range(self.boardHeight):
            for col in range(self.boardWidth):
                print(self.board[self.boardHeight - 1 - row][col], end=" ")
            print(" ")

    def play(self, column: int): # Columns are 1 through boardWidth
        if(column > self.boardWidth or column == 0):
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
